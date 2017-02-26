from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.forms import formset_factory
from . import forms
from . import models


class IndexView(View):
    context = {}

    def get(self, request):
        return render(request, 'registration_site/home_page.html', self.context)

class LoginView(View):
    context = {}
    context['form'] = forms.LoginForm

    def get(self, request):
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

def get_usimc_user(user):
    return models.USIMCUser.objects.filter(user=user)[0]

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
        models.Entry.objects.create(awards_applying_for=awards_applying_for, instrument_category=instrument_category, age_category=age_category, usimc_user=usimc_user)
        return redirect('registration_site:edit_application')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewApplicationView, self).dispatch(*args, **kwargs)

class EditApplicationView(View):
    context = {}
    context['piece_form'] = forms.PieceForm
    context['person_form'] = forms.PersonForm

    def get(self, request):
        return render(request, 'registration_site/edit_application.html', self.context)

    def post(self, request):
        return render(request, 'registration_site/application_steps/new_application_step_1.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditApplicationView, self).dispatch(*args, **kwargs)

class EditPerformersView(View):
    context = {}

    def get(self, request):
        usimc_user = get_usimc_user(request.user)
        Formset = formset_factory(forms.PersonForm)
        initial_performers = models.Person.objects.filter(entry=usimc_user.entry.all()[0])
        initial_data = [{
            'first_name' : 'x.first_name',
            'middle_name' : 'x.middle_name',
            'last_name' : 'x.last_name',
            'email' : 'x.email',
            'phone_number' : 'x.phone_number',
            'instrument' : 'x.instrument',
            'teacher_first_name' : 'x.teacher_first_name',
            'teacher_middle_name' : 'x.teacher_middle_name',
            'teacher_last_name' : 'x.teacher_last_name',
            'teacher_code' : 'x.teacher_code'
            } for x in initial_performers]
        self.context['formset'] = Formset(initial=initial_data)

        return render(request, 'registration_site/person_forms.html', self.context)

    def post(self, request):
        Formset = formset_factory(forms.PersonForm)
        formset = Formset(request.POST)
        if formset.is_valid():
            for form in formset:
                first_name = form.cleaned_data.get('first_name')
                middle_name = form.cleaned_data.get('middle_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                phone_number = form.cleaned_data.get('phone_number')
                instrument = form.cleaned_data.get('instrument')
                teacher_first_name = form.cleaned_data.get('teacher_first_name')
                teacher_middle_name = form.cleaned_data.get('teacher_middle_name')
                teacher_last_name = form.cleaned_data.get('teacher_last_name')
                teacher_code = form.cleaned_data.get('teacher_code')

                person = models.Person.objects.create(first_name = first_name, middle_name = middle_name, last_name = last_name, email = email, phone_number = phone_number, instrument = instrument, teacher_first_name = teacher_first_name, teacher_middle_name = teacher_middle_name, teacher_last_name = teacher_last_name, teacher_code = teacher_code)
            self.context['formset'] = formset
            return render(request, 'registration_site/person_forms.html', self.context)
        else:
            self.context['formset'] = formset
            return render(request, 'registration_site/person_forms.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditPerformersView, self).dispatch(*args, **kwargs)


class ApplicationListView(View):
    context = {}
    context['form'] = forms.EntryForm

    def get(self, request):
        return render(request, 'registration_site/dashboard.html', self.context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ApplicationListView, self).dispatch(*args, **kwargs)


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


