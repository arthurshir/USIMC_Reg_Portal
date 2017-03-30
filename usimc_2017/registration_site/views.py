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
from django.core.mail import send_mail
from . import forms
from . import models
from django.core.exceptions import ObjectDoesNotExist
import django_excel as excel
import csv
import usimc_rules
import usimc_data
from django.http import JsonResponse
import datetime
import pytz
import phonenumbers

# Set your secret key: remember to change this to your live secret key in production
import stripe # See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = "sk_test_xvaC23iBiTk0tb8dEasQT93u"

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
        if form.is_valid():
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = authenticate(username=email, password=password)
            print email, password
            if user is not None:
                login(request, user)
                return redirect('registration_site:dashboard')
            else:
                messages.warning(request, 'Wrong Login Information', extra_tags='login')
                return redirect('registration_site:login')
        else:
            messages.warning(request, 'Form not Valid?', extra_tags='login')
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
            return redirect_register_view_error(request, 'Form not valid?')
        # Check if user exists
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if User.objects.filter(username=email).exists() > 0:
            return redirect_register_view_error(request, 'User with that email already exists')

        # Assert passwords are equal
        if password != password2:
            return redirect_register_view_error(request, 'Passwords do not match')
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
        if not form.is_valid():
            messages.warning(request, "Form is not valid?")
            self.context['form'] = form
            return render(request, 'registration_site/application_submission/application_step1.html', self.context)
        # Create entry
        awards_applying_for = form.cleaned_data['awards_applying_for']
        instrument_category = form.cleaned_data['instrument_category']
        age_category = form.cleaned_data['age_category']
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
        return redirect('registration_site:edit_application', pk=entry.id)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewApplicationView, self).dispatch(*args, **kwargs)

class DeleteApplicationView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        entry = get_object_or_404(models.Entry, pk=self.kwargs['pk']).delete()
        return redirect('registration_site:dashboard')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteApplicationView, self).dispatch(*args, **kwargs)


## Application Submission
class EditApplicationView(View):
    context = {}
    def get(self, request, *args, **kwargs):
        self.load_forms_to_context(request)
        self.load_entry_data_to_context(request)
        return render(request, 'registration_site/application_submission/application_step2.html', self.context)

    def post(self, request, *args, **kwargs):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])
        self.load_entry_data_to_context(request)

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

        # Clean data and check validity
        ensemble_formset_valid = True
        special_cases_valid = True
        if entry.is_ensemble():
            ensemble_formset_valid = self.context['ensemble_member_formset'].is_valid()
        validity_array = [ self.context['piece_formset'].is_valid(), self.context['lead_competitor_form'].is_valid(), self.context['teacher_form'].is_valid(), self.context['contact_form'].is_valid(), ensemble_formset_valid ]

        # Validate special cases -- Birthday & CMTANC
        competitor_forms = [self.context['lead_competitor_form']]
        if entry.is_ensemble():
            competitor_forms += self.context['ensemble_member_formset'].forms
        for form in competitor_forms:
            years = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
            if form.cleaned_data['birthday']:
                birthday = form.cleaned_data['birthday']
                cutoff = usimc_rules.get_age_measurement_date()
                cutoff = cutoff.replace(year=cutoff.year - years) # .date() converts instance from datetime.datetime to datetime (Not sure why this is needed / what is different... TODO: do research)
                if birthday < cutoff:
                    special_cases_valid = False
                    form.add_error('birthday',
                        "Performer must be under " + str(years) + " years old by " + usimc_rules.get_age_measurement_date().strftime("%B %d, %Y"))
        input_cmtanc_code = self.context['teacher_form'].cleaned_data['cmtanc_code']
        if (input_cmtanc_code and input_cmtanc_code not in usimc_data.get_cmtanc_codes()):
            special_cases_valid = False
            self.context['teacher_form'].add_error('cmtanc_code', 'this is an invalid code')    

        # Redirect if not all valid
        validity_array.append(special_cases_valid)
        if not all(validity_array):
            return render(request, 'registration_site/application_submission/application_step2.html', self.context)
        else:
            # Everything is valid:
            # Update single instance objects
            self.context['lead_competitor_form'].save()
            self.context['teacher_form'].save()
            self.context['contact_form'].save()

            # Update pieces
            instances = self.context['piece_formset'].save(commit=False)
            for instance in self.context['piece_formset'].deleted_objects:
                instance.delete()
            for instance in instances:
                instance.entry = entry
                instance.save() 

            # Update ensemble members
            if entry.is_ensemble():
                instances = self.context['ensemble_member_formset'].save(commit=False)
                for instance in self.context['ensemble_member_formset'].deleted_objects:
                    instance.delete()
                for instance in instances:
                    instance.entry = entry
                    instance.save() 

            return redirect(reverse('registration_site:review_submission', kwargs=self.kwargs))

    def load_forms_to_context(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set django forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(prefix=ensemble_member_formset_prefix, queryset=entry.ensemble_members.all())

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

    def get(self, request, *args, **kwargs):
        self.update_entry_context(request)
        if self.context['entry'].submitted:
            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))
        return render(request, 'registration_site/application_submission/review_submission.html', self.context)

    def post(self, request, *args, **kwargs):
        return render(request, 'registration_site/application_submission/review_submission.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReviewSubmissionView, self).dispatch(*args, **kwargs)

class PaymentView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])
        if entry.submitted:
            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))
        self.context['entry'] = entry
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.create_pricing_string()
        return render(request, 'registration_site/application_submission/payment.html', self.context)

    def post(self, request, *args, **kwargs):
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

        if charge.paid:
            entry.submitted = True
            entry.save()

            email_context = {}  
            email_context['entry'] = entry
            email_context['awards_string'] = entry.awards_string()
            email_context['age_category_string'] = entry.age_category_string()
            email_context['instrument_category_string'] = entry.instrument_category_string()
            email_context['is_not_international_string'] = entry.is_not_international_string()
            email_context['lead_performer_birthday_string'] = entry.lead_performer.birthday_string()
            email_context['lead_performer_home_address_string'] = entry.lead_performer.home_address_string()
            email_context['ensemble_members'] = map(lambda x: {
                    'first_name': x.first_name,
                    'last_name': x.last_name,
                    'instrument': x.instrument,
                    'birthday_string': x.birthday_string()
                    }, entry.ensemble_members.all())
            email_context['pieces'] = map(lambda x: {
                    'title': x.title,
                    'opus': xstr(x.opus),
                    'movement': xstr(x.movement),
                    'composer': x.composer,
                    'youtube_link': xstr(x.youtube_link),
                    'length': xstr(x.length)
                    }, entry.pieces.all())
            msg_plain = render_to_string('registration_site/application_submission/confirmation_email.txt', email_context)
            send_mail(
                'USIMC Entry Confirmation',
                msg_plain,
                'usimc2017tech@gmail.com',
                [user.username, 'info@usimc.org'],
                fail_silently=True,
            )
            return redirect(reverse('registration_site:payment_confirmation', kwargs=self.kwargs))
        else:
            self.context['payment_error_message'] = charge.failure_message
            return render(request, 'registration_site/application_submission/payment.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaymentView, self).dispatch(*args, **kwargs)

def payment_confirmation(request, *args, **kwargs):
    context = {}
    usimc_user = get_usimc_user(request.user)
    entry = get_entry(request.user, kwargs['pk'])
    entry.save()
    context['entry'] = entry
    context['email'] = entry.parent_contact.email
    print entry.parent_contact.email
    return render(request, 'registration_site/application_submission/payment_confirmation.html', context)

class EditPerformersView(View):
    context = {}

    # Create Formset
    def get_formset(self, request):
        usimc_user = get_usimc_user(request.user)
        entry = usimc_user.entry.all()[0]
        return self.PersonFormset(queryset=models.Person.objects.filter(entry=entry))

    def get(self, request):
        # Update Formset
        self.context['formset'] = self.get_formset(request)
        return render(request, 'registration_site/person_forms.html', self.context)

    def post(self, request):
        self.context['formset'] = self.PersonFormset(request.POST)
        for form in self.context['formset']:
            if form.is_valid() and form.has_changed():
                person = form.save(commit=False)
                person.entry = models.USIMCUser.objects.filter(user=request.user)[0].entry.all()[0]
                person.save()
            else:
                messages.warning(request, "Form is not valid?")
        self.context['formset'].save()
        # Update to formset with changed data
        self.context['formset'] = self.get_formset(request)
        return render(request, 'registration_site/person_forms.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditPerformersView, self).dispatch(*args, **kwargs)


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
                "age_category": entry.age_category + ",\nbelow " + str(entry.age_category_years()) + " years old",
                "created_at": entry.created_at,
                "submitted": "Submitted" if entry.submitted else "Not Submitted",
                "pk": entry.pk
                })
            return entries_formatted
        usimc_user = get_usimc_user(request.user)
        self.context['user'] = request.user
        self.context['entries'] = usimc_user.entry.all().order_by('created_at')
        self.context['unsubmitted_entries_formatted'] = format_entries(usimc_user.entry.all().filter(submitted=False).order_by('created_at'))
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
            print email, password
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
        response['Content-Disposition'] = 'attachment; filename="entries.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Contact First Name',
            'Contact Last Name',
            'Contact Email',
            'awards_applying_for',
            'instrument_category',
            'age_category',
            'submitted',
            'performers',
            'pieces',
            'created_at',
            'updated_at',
            ])

        entries = models.Entry.objects.all().order_by('instrument_category')
        for entry in entries:
            user = entry.usimc_user.user
            row = []
            # row.append(user.first_name)
            # row.append(user.last_name)
            # row.append(user.email)
            # row.append(map(lambda x: str(models.AWARD_CATEGORIES_DICT[x]), entry.awards_applying_for))
            # row.append(str(usimc_rules.INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES_DICT[entry.instrument_category]))
            # row.append(entry.age_category)
            # row.append(entry.submitted)

            # persons = models.Person.objects.filter(entry=entry)
            # person_column = ""
            # for person in persons:
            #     person_column += str(person.first_name) + ', '
            #     person_column += str(person.middle_name) + ', '
            #     person_column += str(person.last_name) + ', '
            #     person_column += str(person.email) + ', '
            #     person_column += str(person.phone_number) + ', '
            #     person_column += str(person.instrument) + ', '
            #     person_column += str(person.teacher_first_name) + ', '
            #     person_column += str(person.teacher_middle_name) + ', '
            #     person_column += str(person.teacher_last_name) + ', '
            #     person_column += str(person.teacher_code)
            #     person_column += '\n'
            # row.append(person_column)

            # pieces = models.Piece.objects.filter(entry=entry)
            # piece_column = ""
            # for piece in pieces:
            #     piece_column += str(piece.catalogue) + ', '
            #     piece_column += str(piece.title) + ', '
            #     piece_column += str(piece.composer) + ', '
            #     piece_column += str(piece.is_chinese)
            #     piece_column += '\n'
            # row.append(piece_column)

            # row.append(entry.created_at)
            # row.append(entry.updated_at)
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
    return HttpResponse(entry.create_pricing_string_with_custom_values(num_ensemble_members, num_awards))

## Helper Functions
def xstr(s):
    if s is None:
        return ''
    return str(s)
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
PieceFormset = modelformset_factory(models.Piece, form=forms.PieceForm, max_num=4, extra=0, can_delete=True, fields=['title', 'opus', 'movement', 'composer', 'length', 'youtube_link'])
EnsembleMemberFormset = modelformset_factory(models.EnsembleMember, form=forms.EnsembleMemberForm, max_num=20, extra=0, can_delete=True, fields=['first_name', 'last_name', 'instrument', 'birthday'])
# Form prefixes
piece_formset_prefix = 'pieces'
ensemble_member_formset_prefix = 'ensemble_member'
lead_competitor_form_prefix = 'competitor'
teacher_form_prefix = 'teacher'
parent_contact_form_prefix = 'contact'
