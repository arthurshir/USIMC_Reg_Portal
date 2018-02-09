# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from django.core.mail import send_mail, EmailMessage
from . import forms
from . import models
from .models import xstr
from django.core.exceptions import ObjectDoesNotExist
import django_excel as excel
import csv
from . import usimc_rules
from . import usimc_data
from django.http import JsonResponse
import datetime
import pytz
import phonenumbers
from django.conf import settings

# Set your secret key: remember to change this to your live secret key in production
import dotenv
import os
import stripe # See your keys here: https://dashboard.stripe.com/account/apikeys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STRIPE_TEST_PUBLISHABLE_KEY = ''
STRIPE_LIVE_PUBLISHABLE_KEY = ''
if settings.DEBUG:
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
    STRIPE_TEST_PUBLISHABLE_KEY = settings.STRIPE_TEST_PUBLISHABLE_KEY
else:
    stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY
    STRIPE_LIVE_PUBLISHABLE_KEY = settings.STRIPE_LIVE_PUBLISHABLE_KEY

def _cf(value):
    return None if value == '' else value

def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def _cf_int(value):
    int(value) if represents_int(value) else None


class IndexView(View):
    context = {}

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')
        else:
            return redirect('registration_site:login')
        return render(request, 'registration_site/home_page.html', self.context)


## Auth Views
class LogoutView(View):
    context = {}

    def get(self, request):
        logout(request)
        return redirect('registration_site:login')

class LoginView(View):
    context = {}
    context['form'] = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')

        return render(request, 'registration_site/auth/login.html', self.context)

    def post(self, request):
        form = forms.LoginForm(request.POST)

        if not form.is_valid():
            messages.warning(request, 'Please fill all of the fields', extra_tags='login')
            return redirect('registration_site:login')

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('registration_site:dashboard')
        else:
            if User.objects.filter(username=email).exists():
                messages.warning(request, 'This is a wrong password', extra_tags='login')
            else:
                messages.warning(request, 'An account with this email does not exist in our system', extra_tags='login')
            return redirect('registration_site:login')

class RegisterView(View):
    context = {}
    context['form'] = forms.RegistrationForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')
        return render(request, 'registration_site/auth/register.html', self.context)

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        # Assert form is valid
        if not form.is_valid():
            return redirect_register_view_error(request, 'Please fill all of the fields')
        # Check if user exists
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if User.objects.filter(username=email).exists():
            return redirect_register_view_error(request, 'A user with that email already exists')

        # Assert passwords are equal
        if password != password2:
            return redirect_register_view_error(request, 'The passwords do not match')
        # Create User and corresponding USIMCUser instances
        user = User.objects.create(username=email, email=email, password=password)
        user.set_password(password)
        user.save()
        usimc_user = models.USIMCUser.objects.create(user=user)
        login(request, user)
        return redirect('registration_site:dashboard')


## Application Management Views
class DashboardView(View):
    context = {}

    def get(self, request):
        return render(request, 'registration_site/application_management/dashboard.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

class NewApplicationView(View):
    context = {}
    context['form'] = forms.EntryForm

    def get(self, request):
        return render(request, 'registration_site/application_submission/application_step1.html', self.context)

    def post(self, request):
        form = forms.EntryForm(request.POST)
        # Assert form is valid
        if not all(map(lambda x: _cf(x), form['awards_applying_for'].value())):
            messages.warning(request, "Please fill all fields")
            self.context['form'] = form
            return render(request, 'registration_site/application_submission/application_step1.html', self.context)
        # Create entry
        awards_applying_for = [form['awards_applying_for'].value()]
        instrument_category = form['instrument_category'].value()
        age_category = form['age_category'].value()
        usimc_user = get_usimc_user(request.user)
        entry = models.Entry.objects.create(awards_applying_for=awards_applying_for, instrument_category=instrument_category, age_category=age_category, usimc_user=usimc_user)

        # Create Initial Relations
        entry.teacher = models.Teacher.objects.create()
        entry.lead_performer = models.Person.objects.create()
        entry.parent_contact = models.ParentContact.objects.create()
        models.Piece.objects.create(entry = entry)
        entry.save()

        # Ensemble
        if entry.is_ensemble():
            models.EnsembleMember.objects.create(entry = entry)
        return redirect('registration_site:application_part_2', pk=entry.id)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewApplicationView, self).dispatch(*args, **kwargs)

class DeleteApplicationView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        entry = get_object_or_404(models.Entry, pk=self.kwargs['pk'])
        # only allow the entry to be deleted if it has not been submitted yet
        if not entry.submitted:
            entry.delete()
        return redirect('registration_site:dashboard')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteApplicationView, self).dispatch(*args, **kwargs)


## Application Submission
class ApplicationPart2View(View):
    context = {}
    def get(self, request, *args, **kwargs):
        self.load_forms_to_context(request)
        self.load_entry_data_to_context(request)
        return render(request, 'registration_site/application_submission/application_step2.html', self.context)

    def post(self, request, *args, **kwargs):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Collect forms
        self.context['piece_formset'] = PieceFormset(request.POST, prefix=piece_formset_prefix)
        self.context['lead_competitor_form'] = forms.PersonForm(request.POST, prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(request.POST, prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(request.POST, prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        if entry.is_ensemble():
            self.context['ensemble_member_formset'] = EnsembleMemberFormset(request.POST, prefix=ensemble_member_formset_prefix)

        # Save html field data
        entry.is_not_international = request.POST.get('lives-in-united-states') == "1"
        entry.save()

        ## Validate all data and add messages to forms
        entry.teacher.first_name = _cf(self.context['teacher_form']['first_name'].value())
        entry.teacher.last_name = _cf(self.context['teacher_form']['last_name'].value())
        entry.teacher.email = _cf(self.context['teacher_form']['email'].value())
        entry.teacher.cmtanc_code = _cf(self.context['teacher_form']['cmtanc_code'].value())
        print (entry.teacher.cmtanc_code)
        entry.teacher.save()

        entry.parent_contact.first_name = _cf(self.context['contact_form']['first_name'].value())
        entry.parent_contact.last_name = _cf(self.context['contact_form']['last_name'].value())
        entry.parent_contact.email = _cf(self.context['contact_form']['email'].value())
        entry.parent_contact.phone_number = _cf(self.context['contact_form']['phone_number'].value())
        entry.parent_contact.save()

        entry.lead_performer.first_name = _cf(self.context['lead_competitor_form']['first_name'].value())
        entry.lead_performer.last_name = _cf(self.context['lead_competitor_form']['last_name'].value())
        entry.lead_performer.instrument = _cf(self.context['lead_competitor_form']['instrument'].value())
        entry.lead_performer.address = _cf(self.context['lead_competitor_form']['address'].value())
        entry.lead_performer.city = _cf(self.context['lead_competitor_form']['city'].value())
        entry.lead_performer.state = _cf(self.context['lead_competitor_form']['state'].value())
        entry.lead_performer.zip_code = _cf(self.context['lead_competitor_form']['zip_code'].value())
        entry.lead_performer.country = _cf(self.context['lead_competitor_form']['country'].value())
        entry.lead_performer.month = _cf(self.context['lead_competitor_form']['month'].value())
        entry.lead_performer.day = _cf(self.context['lead_competitor_form']['day'].value())
        entry.lead_performer.year = _cf(self.context['lead_competitor_form']['year'].value())
        entry.lead_performer.save()

        if entry.is_ensemble():
            for form in self.context['ensemble_member_formset']:
                contestant = None
                if _cf(form['DELETE'].value()):
                    contestants = models.EnsembleMember.objects.all().filter(pk=_cf(form['id'].value())) 
                    if len(contestants) > 0:
                        contestants[0].delete()
                    del form
                    continue
                elif _cf(form['id'].value()):
                    contestant = models.EnsembleMember.objects.get(pk=_cf(form['id'].value()))
                else:
                    contestant = models.EnsembleMember()
                contestant.first_name = _cf(form['first_name'].value())
                contestant.last_name = _cf(form['last_name'].value())
                contestant.instrument = _cf(form['instrument'].value())
                contestant.month = _cf(form['month'].value())
                contestant.day = _cf(form['day'].value())
                contestant.year = _cf(form['year'].value())
                contestant.entry = entry
                contestant.save()

        for form in self.context['piece_formset']:
            piece = None
            if _cf(form['DELETE'].value()):
                pieces = models.Piece.objects.all().filter(pk=_cf(form['id'].value()))
                if len(pieces) > 0:
                    pieces[0].delete()
                del form
                continue
            elif _cf(form['id'].value()):
                piece = models.Piece.objects.get(pk=_cf(form['id'].value()))
            else:
                piece = models.Piece()

            piece.title = _cf(form['title'].value())
            piece.opus = _cf(form['opus'].value())
            piece.movement = _cf(form['movement'].value())
            piece.composer = _cf(form['composer'].value())
            piece.youtube_link = _cf(form['youtube_link'].value())
            piece.minutes = _cf(form['minutes'].value())
            piece.seconds = _cf(form['seconds'].value())
            piece.entry = entry
            piece.save()

        if request.POST.get('save-form'):
            self.load_forms_to_context(request)
        else:
            # Clean all to allow validation
            self.clean_all_forms(request)
            # Add validation
            self.special_validation_messages(request)
            if request.POST.get('submit-form'):
                self.blank_validation_messages(request)

        self.load_entry_data_to_context(request)
        if request.POST.get('save-form') or not entry.validate():
            return render(request, 'registration_site/application_submission/application_step2.html', self.context)

        return redirect(reverse('registration_site:review_submission', kwargs=self.kwargs))

    def clean_all_forms(self, request):
        entry = get_entry(request.user, self.kwargs['pk'])
        self.context['piece_formset'].is_valid()
        self.context['lead_competitor_form'].is_valid()
        self.context['teacher_form'].is_valid()
        self.context['contact_form'].is_valid()
        if entry.is_ensemble():
            self.context['ensemble_member_formset'].is_valid()


    def special_validation_messages(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Add Validation Messages
        competitor_forms = [self.context['lead_competitor_form']]
        if entry.is_ensemble():
            competitor_forms += self.context['ensemble_member_formset'].forms
        for form in competitor_forms:
            if all([_cf(form['month'].value()), _cf(form['day'].value()), _cf(form['year'].value()) ]):
                birthday_string = _cf(form['month'].value()) + "-" + _cf(form['day'].value()) + "-" + _cf(form['year'].value())
                print ("Birthday String", birthday_string)
                birthday = models.string_to_date(birthday_string) 
                if birthday:
                    if not entry.lead_performer.validate_birthday(birthday):
                        form.add_error('year', "Performer must be at or under " + str(entry.age_category_years()) + " years old by " + usimc_rules.get_age_measurement_date().strftime("%B %d, %Y"))
                else:
                    form.add_error('year', "Wrong format for date")
        input_cmtanc_code = _cf(self.context['teacher_form']['cmtanc_code'].value())
        print (input_cmtanc_code)
        print (entry.teacher.validate_cmtanc_code(input_cmtanc_code))
        if input_cmtanc_code and not entry.teacher.validate_cmtanc_code(input_cmtanc_code):
            self.context['teacher_form'].add_error('cmtanc_code', 'this is an invalid code')    

    def blank_validation_messages(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        def add_blank_error(form_name, field, value):
            if value == None:
                self.context[form_name].add_error(field, 'required')

        def add_blank_error_form(form, field, value):
            if value == None:
                form.add_error(field, 'required')

        add_blank_error('contact_form', 'first_name', entry.parent_contact.first_name)
        add_blank_error('contact_form', 'last_name', entry.parent_contact.last_name)
        add_blank_error('contact_form', 'email', entry.parent_contact.email)
        add_blank_error('contact_form', 'phone_number', entry.parent_contact.phone_number)

        add_blank_error('teacher_form', 'first_name', entry.teacher.first_name)
        add_blank_error('teacher_form', 'last_name', entry.teacher.last_name)
        add_blank_error('teacher_form', 'email', entry.teacher.email)

        add_blank_error('lead_competitor_form', 'first_name', entry.lead_performer.first_name )
        add_blank_error('lead_competitor_form', 'last_name', entry.lead_performer.last_name )
        add_blank_error('lead_competitor_form', 'instrument', entry.lead_performer.instrument )
        add_blank_error('lead_competitor_form', 'address', entry.lead_performer.address )
        add_blank_error('lead_competitor_form', 'city', entry.lead_performer.city )
        add_blank_error('lead_competitor_form', 'state', entry.lead_performer.state )
        add_blank_error('lead_competitor_form', 'zip_code', entry.lead_performer.zip_code )
        add_blank_error('lead_competitor_form', 'country', entry.lead_performer.country )
        add_blank_error('lead_competitor_form', 'month', entry.lead_performer.month )
        add_blank_error('lead_competitor_form', 'day', entry.lead_performer.day )
        add_blank_error('lead_competitor_form', 'year', entry.lead_performer.year )

        if entry.awards_include_youth() and not entry.validate_youth_youtube_link_validation():
            if entry.instrument_category == usimc_rules.INSTRUMENT_CHOICE_CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE \
                or entry.instrument_category == usimc_rules.INSTRUMENT_CHOICE_CHAMBER_ENSEMBLE:
                self.context['piece_formset'][0].add_error(None, 'Must include Youtube Links to at least 1 piece for Young Artist Award for this instrument category.')
            else:
                self.context['piece_formset'][0].add_error(None, 'Must include Youtube Links to at least 2 pieces for Young Artist Award.')

        if entry.is_ensemble():
            for form in self.context['ensemble_member_formset'].forms:
                add_blank_error_form(form, 'first_name', _cf(form['first_name'].value()))
                add_blank_error_form(form, 'last_name', _cf(form['last_name'].value()))
                add_blank_error_form(form, 'instrument', _cf(form['instrument'].value()))
                add_blank_error_form(form, 'month', _cf(form['month'].value()))
                add_blank_error_form(form, 'day', _cf(form['day'].value()))
                add_blank_error_form(form, 'year', _cf(form['year'].value()))

        for form in self.context['piece_formset']:
            add_blank_error_form(form, 'title', _cf(form['title'].value()))
            add_blank_error_form(form, 'composer', _cf(form['composer'].value()))
            add_blank_error_form(form, 'minutes', _cf(form['minutes'].value()))
            add_blank_error_form(form, 'seconds', _cf(form['seconds'].value()))


    def load_forms_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set django forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(prefix=ensemble_member_formset_prefix, queryset=entry.ensemble_members.all().order_by('created_at'))

        # Set html fields
        self.context['lives_in_united_states'] = "1" if entry.is_not_international else "0"

    def load_entry_data_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set other
        self.context['entry'] = entry
        self.context['entry_num_award_categories'] = len(entry.awards_applying_for)
        self.context['entry_award_categories'] = entry.awards_string()
        self.context['entry_instrument_category'] = usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[entry.instrument_category]
        self.context['entry_age_category_years'] = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.create_pricing_string()
        self.context['is_ensemble_application'] = entry.is_ensemble()
        self.context['valid_cmtanc_code'] = entry.teacher.cmtanc_code if entry.teacher.has_valid_cmtanc_code() else False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApplicationPart2View, self).dispatch(*args, **kwargs)

class EditApplicationView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        self.load_forms_to_context(request)
        self.load_entry_data_to_context(request)
        self.context['saved'] = False
        return render(request, 'registration_site/application_management/application_edit.html', self.context)


    def post(self, request, *args, **kwargs):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Collect forms
        self.context['contact_form'] = forms.ParentContactForm(request.POST, prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        self.context['teacher_form'] = forms.TeacherForm(request.POST, prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['lead_competitor_form'] = forms.PersonForm(request.POST, prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        if entry.is_ensemble():
            self.context['ensemble_member_formset'] = EnsembleMemberFormset(request.POST, prefix=ensemble_member_formset_prefix)
        self.context['piece_formset'] = PieceFormset(request.POST, prefix=piece_formset_prefix)

        ## Validate all data and add messages to forms
        contact_form_fields = [_cf(self.context['contact_form']['first_name'].value()), _cf(self.context['contact_form']['first_name'].value()), _cf(self.context['contact_form']['email'].value()), _cf(self.context['contact_form']['phone_number'].value()) ]
        if all(contact_form_fields):
            print ("changing parent data!")
        else:
            print ("Missing field?")

        teacher_form_fields = [_cf(self.context['teacher_form']['first_name'].value()), _cf(self.context['teacher_form']['first_name'].value()), _cf(self.context['teacher_form']['email'].value()) ]
        if all(teacher_form_fields):
            print ("changing teacher data!")
        else:
            print ("Missing field?")

        lead_performer_form_fields = [_cf(self.context['lead_competitor_form']['first_name'].value()), _cf(self.context['lead_competitor_form']['last_name'].value()), _cf(self.context['lead_competitor_form']['instrument'].value()), _cf(self.context['lead_competitor_form']['address'].value()), _cf(self.context['lead_competitor_form']['city'].value()), _cf(self.context['lead_competitor_form']['state'].value()), _cf(self.context['lead_competitor_form']['zip_code'].value()), _cf(self.context['lead_competitor_form']['country'].value()),]
        if all(teacher_form_fields):
            print ("changing lead performer data!")
        else:
            print ("missing Field?")
        if entry.is_ensemble():
            for form in self.context['ensemble_member_formset']:
                ensemble_member_form_fields = [_cf(form['first_name'].value()), _cf(form['last_name'].value()), _cf(form['instrument'].value())]
                if all(ensemble_member_form_fields):
                    print ("changing ensemble member data!")
                else:
                    print ("missing field?")
        has_enough_youtube_links = True
        if entry.awards_include_youth():
            youtube_link_array = []
            for form in self.context['piece_formset']:
                if _cf(form['youtube_link'].value()):
                    youtube_link_array.append( _cf(form['youtube_link'].value()) )
            has_enough_youtube_links = len(youtube_link_array) >= 2
        if not has_enough_youtube_links:
            print ("missing youtube field?")

        for form in self.context['piece_formset']:            
            piece_form_fields = [_cf(form['title'].value()), _cf(form['composer'].value()), _cf(form['minutes'].value()), _cf(form['seconds'].value()), ]
            if all(piece_form_fields):
                print ("changing piece data!")
            else:
                print ("missing field?")

            if has_enough_youtube_links:
                print ("chnging youtube")
            else:
                print ("no youtube")

        self.load_forms_to_context(request)
        self.load_entry_data_to_context(request)
        self.context['saved'] = True
        return render(request, 'registration_site/application_management/application_edit.html', self.context)
   
    def load_forms_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set django forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(prefix=ensemble_member_formset_prefix, queryset=entry.ensemble_members.all().order_by('created_at'))

        # Set html fields
        self.context['lives_in_united_states'] = "1" if entry.is_not_international else "0"

    def load_forms_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set django forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(prefix=ensemble_member_formset_prefix, queryset=entry.ensemble_members.all().order_by('created_at'))

        # Set html fields
        self.context['lives_in_united_states'] = "1" if entry.is_not_international else "0"


    def load_entry_data_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set other
        self.context['entry'] = entry
        self.context['entry_num_award_categories'] = len(entry.awards_applying_for)
        self.context['entry_award_categories'] = entry.awards_string()
        self.context['entry_instrument_category'] = usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[entry.instrument_category]
        self.context['entry_age_category_years'] = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.create_pricing_string()
        self.context['is_ensemble_application'] = entry.is_ensemble()
        self.context['valid_cmtanc_code'] = entry.teacher.cmtanc_code if entry.teacher.has_valid_cmtanc_code() else False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditApplicationView, self).dispatch(*args, **kwargs)

class ReviewSubmissionView(View):
    context = {}

    def update_entry_context(self, request):
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])
        self.context['entry'] = entry
        self.context['entry_award_categories'] = entry.awards_string()
        self.context['entry_instrument_category'] = usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[entry.instrument_category]
        self.context['entry_age_category_years'] = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.create_pricing_string()
        self.context['parent_contact'] = entry.parent_contact.basic_information_string()
        self.context['teacher'] = entry.parent_contact.basic_information_string()
        self.context['ensemble_members'] = [ x.basic_information_string() for x in entry.ensemble_members.all() ]
        self.context['pieces'] = [ x.basic_information_string() for x in entry.pieces.all() ]
        self.context['complete_description_string'] = entry.complete_description_string()

    def get(self, request, *args, **kwargs):
        # Only allow requests for validated entries
        entry = get_entry(request.user, self.kwargs['pk'])
        self.update_entry_context(request)
        if not entry.validate():
            return redirect(reverse('registration_site:application_part_2', kwargs=self.kwargs))

        self.context['agreement_error'] = None

        if self.context['entry'].submitted:
            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))
        return render(request, 'registration_site/application_submission/review_submission.html', self.context)

    def post(self, request, *args, **kwargs):
        # Only allow requests for validated entries
        entry = get_entry(request.user, self.kwargs['pk'])
        self.update_entry_context(request)

        if not entry.validate():
            return redirect(reverse('registration_site:application_part_2', kwargs=self.kwargs))

        input_signature = _cf(request.POST.get('agreement_signature'))
        if not input_signature:
            self.context['agreement_error'] = True
            return render(request, 'registration_site/application_submission/review_submission.html', self.context)
        else:
            entry.signature = input_signature
            print (input_signature)
            entry.save()
            return redirect(reverse('registration_site:pay', kwargs=self.kwargs))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReviewSubmissionView, self).dispatch(*args, **kwargs)

class PaymentView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        # Only allow requests for validated entries
        entry = get_entry(request.user, self.kwargs['pk'])
        if not entry.validate():
            return redirect(reverse('registration_site:application_part_2', kwargs=self.kwargs))
        if not entry.signature:
            return redirect(reverse('registration_site:review_submission', kwargs=self.kwargs))

        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])
        if entry.submitted:
            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))

        if settings.DEBUG:
            self.context['stripe_publishable_key'] = STRIPE_TEST_PUBLISHABLE_KEY
        else:
            self.context['stripe_publishable_key'] = STRIPE_LIVE_PUBLISHABLE_KEY

        self.context['entry'] = entry
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.create_pricing_string()
        return render(request, 'registration_site/application_submission/payment.html', self.context)

    def post(self, request, *args, **kwargs):
        # Only allow requests for validated entries
        entry = get_entry(request.user, self.kwargs['pk'])
        if not entry.validate():
            return redirect(reverse('registration_site:application_part_2', kwargs=self.kwargs))

        user = request.user
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Token is created using Stripe.js or Checkout!
        # Get the payment token submitted by the form:
        token = request.POST['stripeToken'] # Using Flask

        # Charge the user's card:
        charge = stripe.Charge.create(
          amount=entry.calculate_price(),
          currency="usd",
          description=entry.basic_information_string(),
          source=token,
        )

        if charge.paid:
            usimc_charge = models.Charge()
            usimc_charge.usimc_user = usimc_user
            usimc_charge.entry = entry
            usimc_charge.charge_id = charge.id
            usimc_charge.charge_amount = charge.amount
            usimc_charge.charge_customer = xstr(charge.customer)
            usimc_charge.charge_description = xstr(charge.description)
            usimc_charge.charge_failure_message = xstr(charge.failure_message)
            usimc_charge.charge_paid = charge.paid
            usimc_charge.charge_receipt_email = xstr(charge.receipt_email)
            usimc_charge.save()

            entry.submitted = True
            entry.save()

            email = EmailMessage(
                'USIMC Entry Confirmation' + (' - TESTING (Not a real applicant)' if settings.DEBUG else ''),
                entry.confirmation_email_string(),
                'usimc2017tech@gmail.com',
                [user.username, 'info@usimc.org'],
            )
            email.attach_file(os.path.join(BASE_DIR, 'USIMC_Checklist.pdf'))
            if (not settings.DEBUG) or (settings.DEBUG and settings.ENABLE_EMAILS_FOR_DEBUG):
                email.send()

            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))
        else:
            self.context['payment_error_message'] = charge.failure_message
            return render(request, 'registration_site/application_submission/payment.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentView, self).dispatch(*args, **kwargs)

def payment_confirmation(request, *args, **kwargs):
    # Only allow requests for validated entries
    entry = get_entry(request.user, kwargs['pk'])
    if not entry.validate():
        return redirect(reverse('registration_site:application_part_2', kwargs=kwargs))

    context = {}
    usimc_user = get_usimc_user(request.user)
    entry = get_entry(request.user, kwargs['pk'])
    entry.save()
    context['entry'] = entry
    context['email'] = entry.parent_contact.email
    return render(request, 'registration_site/application_submission/payment_confirmation.html', context)

class ApplicationListView(View):
    context = {}
    context['entries'] = []

    def get(self, request):
        def format_entries(entries):
            entries_formatted = []
            for entry in entries:
                entries_formatted.append({
                "awards": reduce((lambda x, y: x + ',\n' + y), entry.award_strings()),
                "instrument_category": entry.instrument_category_string(),
                "age_category": entry.age_category + ",\nat or under " + str(entry.age_category_years()) + " years old",
                "created_at": entry.created_at,
                "status": "Canceled" if entry.canceled else ("Submitted" if entry.submitted else "Not Submitted"),
                "pk": entry.pk
                })
            return entries_formatted
        usimc_user = get_usimc_user(request.user)
        self.context['user'] = request.user
        self.context['entries'] = usimc_user.entry.all().order_by('created_at')
        self.context['unsubmitted_entries_formatted'] = format_entries(usimc_user.entry.all().filter(submitted=False).order_by('-created_at'))
        self.context['submitted_entries_formatted'] = format_entries(usimc_user.entry.all().filter(submitted=True).order_by('-created_at'))

        return render(request, 'registration_site/application_management/application_list.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApplicationListView, self).dispatch(*args, **kwargs)


## Admin Views
class AdminLoginView(View):
    context = {}
    context['form'] = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:admin_dashboard')

        return render(request, 'registration_site/auth/login.html', self.context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('registration_site:dashboard')
            else:
                messages.warning(request, 'Wrong Login Information', extra_tags='login')
                return redirect('registration_site:login')
        else:
            messages.warning(request, 'Form not Valid?', extra_tags='login')
            return redirect('registration_site:login')

class DownloadEntriesView(View ):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="ensemble_entries.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Parent: First Name',
            'Parent: Last Name',
            'Parent: Email',
            'Parent: Phone Number',

            'Award',
            'Instrument Category',
            'Age Category',
            'Age Category (years)',
            'Lead Competitor: Address',

            'Teacher: First Name',
            'Teacher: Last Name',
            'Teacher: Email',
            'Teacher: CMTANC Code',

            'Competitors: First Name',
            'Competitors: Last Name',
            'Competitors: Instrument',
            'Competitors: Birthday',

            'Pieces: Title',
            'Pieces: Opus',
            'Pieces: Movement',
            'Pieces: Composer',
            'Pieces: Youtube_link',
            'Pieces: Minutes',
            'Pieces: Seconds',

            'created_at',
            'updated_at',
            ])

        print (models.Entry.objects.all().filter(submitted=True).order_by('instrument_category'))
        entries = filter(lambda x: x.is_ensemble(), models.Entry.objects.all().filter(submitted=True).order_by('instrument_category'))
        for entry in entries:
            usimc_user = entry.usimc_user
            user = entry.usimc_user.user
            row = []

            # Parent Contact
            row.append( entry.parent_contact.first_name )
            row.append( entry.parent_contact.last_name )
            row.append( entry.parent_contact.email )
            row.append( entry.parent_contact.phone_number )

            # Entry Information
            row.append( entry.awards_string() )
            row.append( entry.instrument_category_string() )
            row.append( entry.age_category )
            row.append( entry.age_category_years() )

            # Teacher Information
            row.append( entry.teacher.first_name )
            row.append( entry.teacher.last_name )
            row.append( entry.teacher.email )
            row.append( entry.teacher.cmtanc_code )

            # Lead Performer Address
            row.append( entry.lead_performer.living_address() )

            # Ensemble Members
            ensemble_members = [entry.lead_performer].append(entry.ensemble_members.all())
            print (ensemble_members)
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.first_name, ensemble_members ) ))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.last_name, ensemble_members ) ))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.instrument, ensemble_members ) ))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.birthday(), ensemble_members ) ))

            pieces = entry.pieces.all()
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.title, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.opus, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.movement, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.composer, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.youtube_link, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.minutes, pieces)))
            row.append( reduce(lambda x, y: x + "\n" + y, map(lambda x: x.seconds, pieces)))

            row.append(entry.created_at)
            row.append(entry.updated_at)
            writer.writerow(row)

        return response


## REST API

def redirect_register_view_error(request, message):
    messages.warning(request, message, extra_tags='register')
    return redirect('registration_site:register')

def rules_json(request) :
    return JsonResponse(usimc_rules.RAW_JSON)

def create_pricing_string(request):
    entry = get_entry(request.user, request.GET['pk'])
    num_ensemble_members = int(request.GET['num_ensemble_members'])
    num_awards = int(request.GET['num_awards'])
    is_not_international = (request.GET['is_not_international']) == '1'
    return HttpResponse(entry.create_pricing_string_with_custom_values(num_ensemble_members, num_awards, is_not_international, entry.teacher.cmtanc_code))

## Helper Functions
def get_entry(user, pk):
    usimc_user = models.USIMCUser.objects.filter(user=user)[0]
    return usimc_user.entry.get(pk=pk)
def get_usimc_user(user):
    return models.USIMCUser.objects.filter(user=user)[0]
def get_piece(user, pk):
    return models.Piece.objects.get(entry=get_entry(user, pk), pk=pk)[0]
def get_performer(user, pk):
    return models.Performer.objects.get(entry=get_entry(user, pk), pk=pk)[0]

## Constants
# Formset factories
PieceFormset = modelformset_factory(models.Piece, form=forms.PieceForm, max_num=20, extra=0, can_delete=True, fields=['title', 'opus', 'movement', 'composer', 'minutes', 'seconds', 'youtube_link'])
EnsembleMemberFormset = modelformset_factory(models.EnsembleMember, form=forms.EnsembleMemberForm, max_num=20, extra=0, can_delete=True, fields=['first_name', 'last_name', 'instrument', 'month', 'day', 'year'])
# Form prefixes
piece_formset_prefix = 'pieces'
ensemble_member_formset_prefix = 'ensemble_member'
lead_competitor_form_prefix = 'competitor'
teacher_form_prefix = 'teacher'
parent_contact_form_prefix = 'contact'
