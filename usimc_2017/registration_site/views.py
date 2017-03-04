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

class IndexView(View):
    context = {}

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('registration_site:dashboard')
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
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if User.objects.filter(username=email).exists() > 0:
            return redirect_register_view_error(request, 'User with that email already exists')

        # Assert passwords are equal
        if password != password2:
            return redirect_register_view_error(request, 'Passwords do not match')
        # Create User and corresponding USIMCUser instances
        user = User.objects.create(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
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
        # Create Entry
        awards_applying_for = form.cleaned_data['awards_applying_for']
        instrument_category = form.cleaned_data['instrument_category']
        age_category = form.cleaned_data['age_category']
        usimc_user = models.USIMCUser.objects.filter(user=request.user)[0]
        entry = models.Entry.objects.create(awards_applying_for=awards_applying_for, instrument_category=instrument_category, age_category=age_category, usimc_user=usimc_user)

        models.Piece.objects.create(entry = entry)
        models.Person.objects.create(entry = entry)

        return redirect('registration_site:edit_application', pk=entry.id)

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


class EditApplicationView(View):
    context = {}
    personFormsetPrefix = 'performers'
    pieceFormsetPrefix = 'pieces'
    PersonFormset = modelformset_factory(models.Person, extra=0, can_delete=True, fields=['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'instrument', 'teacher_first_name', 'teacher_middle_name', 'teacher_last_name', 'teacher_code'])
    PieceFormset = modelformset_factory(models.Piece, max_num=3, extra=0, can_delete=True, fields=['catalogue', 'title', 'composer', 'is_chinese',])

    def update_forms_and_formsets(self, request):
        usimc_user = models.USIMCUser.objects.filter(user=request.user)[0]
        entry = usimc_user.entry.get(pk=self.kwargs['pk'])
        self.context['entry_form'] = forms.EntryForm(prefix='entry', instance=entry)
        self.context['performer_formset'] = self.PersonFormset(prefix=self.personFormsetPrefix, queryset=models.Person.objects.filter(entry=entry).order_by('created_at'))
        self.context['piece_formset'] = self.PieceFormset(prefix=self.pieceFormsetPrefix, queryset=models.Piece.objects.filter(entry=entry).order_by('created_at'))

    def get(self, request, *args, **kwargs):
        self.update_forms_and_formsets(request)
        return render(request, 'registration_site/edit_application.html', self.context)

    def post(self, request, *args, **kwargs):
        piecesFormset = self.PieceFormset(request.POST, prefix=self.pieceFormsetPrefix)
        performersFormset = self.PersonFormset(request.POST, prefix=self.personFormsetPrefix)
        print piecesFormset.data
        if all([piecesFormset.is_valid(), performersFormset.is_valid()]):
            for form in piecesFormset:
                if form.cleaned_data.get('DELETE'):
                    try:
                        piece = form.instance
                        piece.delete()
                    except ObjectDoesNotExist:
                        pass
                else:
                    piece = form.save(commit=False)
                    piece.entry = get_entry(request.user, self.kwargs['pk'])
                    piece.save()
            for form in performersFormset:
                if form.cleaned_data.get('DELETE'):
                    try:
                        performer = form.instance
                        performer.delete()
                    except ObjectDoesNotExist:
                        pass
                else:
                    performer = form.save(commit=False)
                    performer.entry = get_entry(request.user, self.kwargs['pk'])
                    performer.save()
        else:
            print piecesFormset.errors
            print performersFormset.errors
        self.update_forms_and_formsets(request)
        return render(request, 'registration_site/edit_application.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditApplicationView, self).dispatch(*args, **kwargs)

class EditPerformersView(View):
    context = {}
    # Create Formset Factory
    PersonFormset = modelformset_factory(models.Person, can_delete=True, fields=['first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'instrument', 'teacher_first_name', 'teacher_middle_name', 'teacher_last_name', 'teacher_code'])

    # Create Formset
    def get_formset(self, request):
        usimc_user = models.USIMCUser.objects.filter(user=request.user)[0]
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
        usimc_user = models.USIMCUser.objects.filter(user=request.user)[0]
        self.context['entries'] = usimc_user.entry.all().order_by('created_at')
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

        entries = models.Entry.objects.all()
        for entry in entries:
            user = entry.usimc_user.user
            row = []
            row.append(user.first_name)
            row.append(user.last_name)
            row.append(user.email)
            row.append(map(lambda x: str(models.AWARD_CATEGORIES_DICT[x]), entry.awards_applying_for))
            row.append(str(models.PERFORMER_CATEGORIES_DICT[entry.instrument_category]))
            row.append(entry.age_category)
            row.append(entry.submitted)

            persons = models.Person.objects.filter(entry=entry)
            person_column = ""
            for person in persons:
                person_column += str(person.first_name) + ', '
                person_column += str(person.middle_name) + ', '
                person_column += str(person.last_name) + ', '
                person_column += str(person.email) + ', '
                person_column += str(person.phone_number) + ', '
                person_column += str(person.instrument) + ', '
                person_column += str(person.teacher_first_name) + ', '
                person_column += str(person.teacher_middle_name) + ', '
                person_column += str(person.teacher_last_name) + ', '
                person_column += str(person.teacher_code)
                person_column += '\n'
            row.append(person_column)

            pieces = models.Piece.objects.filter(entry=entry)
            piece_column = ""
            for piece in pieces:
                piece_column += str(piece.catalogue) + ', '
                piece_column += str(piece.title) + ', '
                piece_column += str(piece.composer) + ', '
                piece_column += str(piece.is_chinese)
                piece_column += '\n'
            row.append(piece_column)

            row.append(entry.created_at)
            row.append(entry.updated_at)
            writer.writerow(row)

        return response

# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.decorators import login_required
# from .forms import UserSigninForm, UserSignupForm, ParentForm, PerformerForm, TeacherForm, PieceForm, ChinesePieceForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.forms.models import formset_factory
# from .models import Performer, Profile, Parent, Teacher, Piece, ChinesePiece
# import json

# def index(request):
#     return HttpResponse("Hello, world!")

# def dashboard(request):
#     profile = Profile.objects.get(user = request.user)
#     performer = Performer.objects.get(owningProfile = profile)

#     if request.method == "POST":
#         performerForm = PerformerForm(request.POST, instance=performer, prefix="performer")
#         teacherForm = TeacherForm(request.POST, instance=performer._teacher, prefix="teacher")
#         pieceForm1 = PieceForm(request.POST, instance=performer.piece1, prefix="piece1")
#         pieceForm2 = PieceForm(request.POST, instance=performer.piece2, prefix="piece2")
#         chinesePieceForm = ChinesePieceForm(request.POST, instance=performer.chinesePiece, prefix="chinesePiece")
#         parentForm = ParentForm(request.POST, instance=profile.parent, prefix="parent")

#         data = {}
#         if performerForm.is_valid() and teacherForm.is_valid() and pieceForm1.is_valid() and pieceForm2.is_valid() and chinesePieceForm.is_valid() and parentForm.is_valid():
#             performerForm.save()
#             teacherForm.save()
#             pieceForm1.save()
#             pieceForm2.save()
#             chinesePieceForm.save()
#             parentForm.save()
#             data['success'] = True
#             print("Form should be saved")
#         else:
#             data['success'] = False
#             data['error'] = "Invalid Form:\n performerForm: {}\nteacherForm: {}\npieceForm1: {}\npieceForm2: {}\nchinesePieceForm: {}\nparentForm: {}\n".format(performerForm.errors,teacherForm.errors,pieceForm1.errors,pieceForm2.errors,chinesePieceForm.errors,parentForm.errors)
            
#         return HttpResponse(json.dumps(data), content_type="application/json")

#     else:
#         context = {}
#         context['performerForm'] = PerformerForm(instance=performer, prefix="performer")
#         context['teacherForm'] = TeacherForm(instance=performer._teacher, prefix="teacher")
#         context['pieceForm1'] = PieceForm(instance=performer.piece1, prefix="piece1")
#         context['pieceForm2'] = PieceForm(instance=performer.piece2, prefix="piece2")
#         context['chinesePieceForm'] = ChinesePieceForm(instance=performer.chinesePiece, prefix="chinesePiece")

#         context['parentForm'] = ParentForm(instance=profile.parent, prefix="parent")
#         return render(request, 'registration_site/dashboard.html', context)

# def login_view(request):
#     if request.method == "POST":
#         form = UserSigninForm(request.POST)
#         if form.is_valid():
#             email = request.POST.get('email', '')
#             password = request.POST.get('password', '')

#             user = authenticate(username=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('registration_site:dashboard')
#             else:
#                 messages.warning(request, 'Wrong Login Information', extra_tags='login')
#                 return redirect('registration_site:login')
#         else:
#             messages.warning(request, 'Wrong Login Information', extra_tags='login')
#             return redirect('registration_site:login')
#     else:
#         context = {}
#         context['user_form'] = UserSigninForm()
#         context['panel_title'] = 'Sign in'
#         return render(request, 'registration_site/sign_in.html', context)

# def signup_view(request):
#     if request.method == "POST":
#         form = UserSignupForm(request.POST)
#         if form.is_valid():
#             first_name = request.POST.get('first_name', '')
#             last_name = request.POST.get('last_name', '')
#             email = request.POST.get('email', '')
#             password = request.POST.get('password', '')
#             confirm_password = request.POST.get('confirm_password', '')

#             if not '@' in email:
#                 messages.warning(request, 'Not an email address', extra_tags='signup')
#                 return redirect('registration_site:signup')

#             if User.objects.filter(username=email).exists():
#                 messages.warning(request, 'A User for {} already exists'.format(email), extra_tags='signup')
#                 return redirect('registration_site:signup')

#             if password != confirm_password: 
#                 messages.warning(request, 'Passwords do not match', extra_tags='signup')
#                 return redirect('registration_site:signup')

#             ## Instantiate Initial User Objects
#             # Profile
#             user = createOrUpdateDjangoUser(email, password, first_name, last_name)
#             parent = Parent.objects.create()
#             profile = Profile.objects.create(user = user, parent=parent)
#             # Performer
#             teacher = Teacher.objects.create()
#             piece1 = Piece.objects.create()
#             piece2 = Piece.objects.create()
#             chinesePiece = ChinesePiece.objects.create()
#             performer = Performer.objects.create(_teacher=teacher, piece1=piece1, piece2=piece2, chinesePiece=chinesePiece, owningProfile=profile)


#             login(request, user)
#             return redirect('registration_site:dashboard')
#         else:
#             messages.warning(request, 'Wrong Signup Information', extra_tags='signup')
#             return redirect('registration_site:signup')
#     else:
#         context = {}
#         context['user_form'] = UserSignupForm()
#         context['panel_title'] = 'Sign up'
#         return render(request, 'registration_site/sign_in.html', context)

# def createOrUpdateDjangoUser(email, password, first_name, last_name):
#     try:
#         user = User.objects.get(username=email)
#         user.set_password(password)
#     except User.DoesNotExist:
#         user = User.objects.create_user(username=email, password=password)
#     user.first_name = first_name
#     user.last_name = last_name
#     user.save()
#     return user


