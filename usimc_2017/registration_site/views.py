from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory
from django.forms.models import modelformset_factory
from . import forms
from . import models
from django.core.exceptions import ObjectDoesNotExist
import django_excel as excel
import csv
import usimc_rules
import usimc_data
from django.http import JsonResponse
import datetime
import phonenumbers

PieceFormset = modelformset_factory(models.Piece, form=forms.PieceForm, max_num=4, extra=0, can_delete=True, fields=['title', 'opus', 'movement', 'composer', 'length', 'is_chinese',])
EnsembleMemberFormset = modelformset_factory(models.EnsembleMember, form=forms.EnsembleMemberForm, max_num=20, extra=0, can_delete=True, fields=['first_name', 'last_name', 'instrument', 'birthday'])

piece_formset_prefix = 'pieces'
ensemble_member_formset_prefix = 'ensemble_member'
lead_competitor_form_prefix = 'competitor'
teacher_form_prefix = 'teacher'
parent_contact_form_prefix = 'contact'

class IndexView(View):
    context = {}

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')
        else:
            return redirect('registration_site:login')
        return render(request, 'registration_site/home_page.html', self.context)

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

        return render(request, 'registration_site/login.html', self.context)

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

def redirect_register_view_error(request, message):
    messages.warning(request, message, extra_tags='register')
    return redirect('registration_site:register')

class RegisterView(View):
    context = {}
    context['form'] = forms.RegistrationForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')
        return render(request, 'registration_site/register.html', self.context)

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

class DashboardView(View):
    context = {}

    def get(self, request):
        return render(request, 'registration_site/dashboard.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

class NewApplicationView(View):
    context = {}
    context['form'] = forms.EntryForm

    def get(self, request):
        return render(request, 'registration_site/create_new_application.html', self.context)

    def post(self, request):
        form = forms.EntryForm(request.POST)
        # Assert form is valid
        if not form.is_valid():
            messages.warning(request, "Form is not valid?")
            self.context['form'] = form
            return render(request, 'registration_site/create_new_application.html', self.context)
        # Create entry
        awards_applying_for = form.cleaned_data['awards_applying_for']
        instrument_category = form.cleaned_data['instrument_category']
        age_category = form.cleaned_data['age_category']
        is_not_international = form.cleaned_data['is_not_international']
        usimc_user = get_usimc_user(request.user)
        entry = models.Entry.objects.create(awards_applying_for=awards_applying_for, instrument_category=instrument_category, age_category=age_category, usimc_user=usimc_user, is_not_international=is_not_international)

        # Create Initial Relations
        entry.teacher = models.Teacher.objects.create()
        entry.lead_performer = models.Person.objects.create()
        entry.parent_contact = models.ParentContact.objects.create()
        models.Piece.objects.create(entry = entry)
        entry.save()

        # Ensemble
        if entry.is_ensemble():
            models.EnsembleMember.objects.create(entry = entry)
            return redirect('registration_site:edit_ensemble_application', pk=entry.id)
        else:
            return redirect('registration_site:edit_solo_application', pk=entry.id)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewApplicationView, self).dispatch(*args, **kwargs)

def get_entry(user, pk):
    usimc_user = models.USIMCUser.objects.filter(user=user)[0]
    return usimc_user.entry.get(pk=pk)

def get_usimc_user(user):
    return models.USIMCUser.objects.filter(user=user)[0]

def get_piece(user, pk):
    return models.Piece.objects.get(entry=get_entry(user, pk), pk=pk)[0]

def get_performer(user, pk):
    return models.Performer.objects.get(entry=get_entry(user, pk), pk=pk)[0]

def edit_application_redirect(request, pk):
    entry = get_entry(request.user, pk)
    if entry.is_ensemble():
        return redirect('registration_site:edit_ensemble_application', pk=entry.id)
    else:
        return redirect('registration_site:edit_solo_application', pk=entry.id)


class EditSoloApplicationView(View):
    context = {}

    def update_forms_and_formsets(self, request):
        # Retrieve user and entry, and other
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry.parent_contact)

        # Set other
        self.context['entry'] = entry
        self.context['entry_award_categories'] = entry.awards_string()
        self.context['entry_instrument_category'] = usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[entry.instrument_category]
        self.context['entry_age_category_years'] = entry.age_category_years()
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.calculate_price_string()

    def get(self, request, *args, **kwargs):
        self.update_forms_and_formsets(request)
        return render(request, 'registration_site/edit_solo_application.html', self.context)

    def post(self, request, *args, **kwargs):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Collect forms
        self.context['piece_formset'] = PieceFormset(request.POST, prefix=piece_formset_prefix)
        self.context['lead_competitor_form'] = forms.PersonForm(request.POST, prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(request.POST, prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(request.POST, prefix=parent_contact_form_prefix, instance=entry.parent_contact)

        # Check all forms are valid
        if not all([self.context['piece_formset'].is_valid(), self.context['lead_competitor_form'].is_valid(), self.context['teacher_form'].is_valid(), self.context['contact_form'].is_valid(),]):
            return render(request, 'registration_site/edit_solo_application.html', self.context)
        else:
            # Birthday validation
            if self.context['lead_competitor_form'].cleaned_data['birthday']:
                years = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
                birthday = self.context['lead_competitor_form'].cleaned_data['birthday'].date()
                cutoff = usimc_rules.get_age_measurement_date()
                cutoff = cutoff.replace(year=cutoff.year - years).date() # .date() converts instance from datetime.datetime to datetime (Not sure why this is needed / what is different... TODO: do research)
                if birthday < cutoff:
                    self.context['lead_competitor_form'].add_error('birthday',
                        "Performer must be under " + str(years) + " years old by " + usimc_rules.get_age_measurement_date().strftime("%B %d, %Y"))
                    return render(request, 'registration_site/edit_solo_application.html', self.context)

            # CMTANC code validation
            cmtanc_codes = usimc_data.get_cmtanc_codes()
            input_cmtanc_code = self.context['teacher_form'].cleaned_data['cmtanc_code']
            print input_cmtanc_code, cmtanc_codes
            print input_cmtanc_code in cmtanc_codes
            if (input_cmtanc_code and input_cmtanc_code not in cmtanc_codes):
                print "invalid code"
                self.context['teacher_form'].add_error('cmtanc_code', 'this is an invalid code')
                return render(request, 'registration_site/edit_solo_application.html', self.context)

            # Update single instance objects
            self.context['lead_competitor_form'].save()
            self.context['teacher_form'].save()
            self.context['contact_form'].save()

            # Update Pieces
            instances = self.context['piece_formset'].save(commit=False)
            for instance in self.context['piece_formset'].deleted_objects:
                instance.delete()
            for instance in instances:
                instance.entry = entry
                instance.save() 

            # Refresh with new forms
            self.update_forms_and_formsets(request)
            return render(request, 'registration_site/edit_solo_application.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditSoloApplicationView, self).dispatch(*args, **kwargs)

class EditEnsembleApplicationView(View):
    context = {}

    def update_forms_and_formsets(self, request):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Set Forms
        self.context['piece_formset'] = PieceFormset(prefix=piece_formset_prefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))
        self.context['lead_competitor_form'] = forms.PersonForm(prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(prefix=parent_contact_form_prefix, instance=entry)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(prefix=ensemble_member_formset_prefix, queryset=entry.ensemble_members.all())

        # Set other
        self.context['entry'] = entry
        self.context['entry_award_categories'] = entry.awards_string()
        self.context['entry_instrument_category'] = usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[entry.instrument_category]
        self.context['entry_age_category_years'] = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
        self.context['calculated_price'] = entry.calculate_price()
        self.context['calculated_price_string'] = entry.calculate_price_string()

    def get(self, request, *args, **kwargs):
        self.update_forms_and_formsets(request)
        return render(request, 'registration_site/edit_ensemble_application.html', self.context)

    def post(self, request, *args, **kwargs):
        # Retrieve user and entry
        usimc_user = get_usimc_user(request.user)
        entry = get_entry(request.user, self.kwargs['pk'])

        # Collect forms
        self.context['piece_formset'] = PieceFormset(request.POST, prefix=piece_formset_prefix)
        self.context['lead_competitor_form'] = forms.PersonForm(request.POST, prefix=lead_competitor_form_prefix, instance=entry.lead_performer)
        self.context['teacher_form'] = forms.TeacherForm(request.POST, prefix=teacher_form_prefix, instance=entry.teacher)
        self.context['contact_form'] = forms.ParentContactForm(request.POST, prefix=parent_contact_form_prefix, instance=entry.parent_contact)
        self.context['ensemble_member_formset'] = EnsembleMemberFormset(request.POST, prefix=ensemble_member_formset_prefix)

        if not all([self.context['piece_formset'].is_valid(), self.context['lead_competitor_form'].is_valid(), self.context['teacher_form'].is_valid(), self.context['contact_form'].is_valid(), self.context['ensemble_member_formset'].is_valid()]):
            return render(request, 'registration_site/edit_ensemble_application.html', self.context)
        else:
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
            instances = self.context['ensemble_member_formset'].save(commit=False)
            for instance in self.context['ensemble_member_formset'].deleted_objects:
                instance.delete()
            for instance in instances:
                instance.entry = entry
                instance.save() 

            # Refresh with new forms and render
            # self.update_forms_and_formsets(request) # TODO: Find out if you actually do need this

            # Validate birthdays
            invalid_birthday_detected = False
            forms_to_check = [self.context['lead_competitor_form']]
            forms_to_check += self.context['ensemble_member_formset'].forms
            for form in forms_to_check:
                years = usimc_rules.get_instrument_category_age_rules(entry.instrument_category)[entry.age_category]
                if form.cleaned_data['birthday']:
                    birthday = form.cleaned_data['birthday']
                    cutoff = usimc_rules.get_age_measurement_date()
                    cutoff = cutoff.replace(year=cutoff.year - years).date() # .date() converts instance from datetime.datetime to datetime (Not sure why this is needed / what is different... TODO: do research)
                    if birthday < cutoff:
                        form.add_error('birthday',
                            "Performer must be under " + str(years) + " years old by " + usimc_rules.get_age_measurement_date().strftime("%B %d, %Y"))

            return render(request, 'registration_site/edit_ensemble_application.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditEnsembleApplicationView, self).dispatch(*args, **kwargs)

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
        print request.POST
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
        usimc_user = get_usimc_user(request.user)
        self.context['user'] = request.user
        self.context['entries'] = usimc_user.entry.all().order_by('created_at')

        unsubmitted_entries = usimc_user.entry.all().filter(submitted=False).order_by('created_at')
        unsubmitted_entries_formatted = []
        for entry in unsubmitted_entries:
            unsubmitted_entries_formatted.append({
            "awards": reduce((lambda x, y: x + ',\n' + y), entry.award_strings()),
            "instrument_category": entry.instrument_category_string(),
            "age_category": entry.age_category + ",\nbelow " + str(entry.age_category_years()) + " years old",
            "created_at": entry.created_at,
            "submitted": "Submitted" if entry.submitted else "Not Submitted",
            "pk": entry.pk
            })
        self.context['unsubmitted_entries_formatted'] = unsubmitted_entries_formatted


        return render(request, 'registration_site/application_list.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApplicationListView, self).dispatch(*args, **kwargs)

class DeleteApplicationView(View):
    context = {}

    def get(self, request, *args, **kwargs):
        entry = get_object_or_404(models.Entry, pk=self.kwargs['pk']).delete()
        return redirect('registration_site:dashboard')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteApplicationView, self).dispatch(*args, **kwargs)


# Admin Views

class AdminLoginView(View):
    context = {}
    context['form'] = forms.LoginForm

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:admin_dashboard')

        return render(request, 'registration_site/login.html', self.context)

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

def rules_json(request) :
    return JsonResponse(usimc_rules.RAW_JSON)
