from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserSigninForm, UserSignupForm, ParentForm, PerformerForm, TeacherForm, PieceForm, PieceFormSetHelper
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms.models import formset_factory

def index(request):
    return HttpResponse("Hello, world!")

def dashboard(request):
    context = {}
    context['performerForm'] = PerformerForm()
    context['teacherForm'] = TeacherForm()
    context['pieceFormSet'] = formset_factory(PieceForm, extra=2)()
    context['pieceFormSetHelper'] = PieceFormSetHelper()

    context['parentForm'] = ParentForm()
    return render(request, 'registration_site/dashboard.html', context)

def login_view(request):
	if request.method == "POST":
		form = UserSigninForm(request.POST)
		if form.is_valid():
			email = request.POST.get('email', '')
			password = request.POST.get('password', '')

			user = authenticate(username=email, password=password)
			if user:
				login(request, user)
				return redirect('registration_site:dashboard')
			else:
				messages.warning(request, 'Wrong Login Information', extra_tags='login')
				return redirect('registration_site:login')
		else:
			messages.warning(request, 'Wrong Login Information', extra_tags='login')
			return redirect('registration_site:login')
	else:
	    context = {}
	    context['user_form'] = UserSigninForm()
	    context['panel_title'] = 'Sign in'
	    return render(request, 'registration_site/sign_in.html', context)

def signup_view(request):
	if request.method == "POST":
		form = UserSignupForm(request.POST)
		if form.is_valid():
			first_name = request.POST.get('first_name', '')
			last_name = request.POST.get('last_name', '')
			email = request.POST.get('email', '')
			password = request.POST.get('password', '')
			confirm_password = request.POST.get('confirm_password', '')

			if User.objects.filter(username=email).exists():
				messages.warning(request, 'A User for {} already exists'.format(email), extra_tags='signup')
				return redirect('registration_site:signup')

			if password != confirm_password: 
				messages.warning(request, 'Passwords do not match', extra_tags='signup')
				return redirect('registration_site:signup')

			user = createOrUpdateDjangoUser(email, password, first_name, last_name)
			login(request, user)
			return redirect('registration_site:dashboard')
		else:
			messages.warning(request, 'Wrong Signup Information', extra_tags='signup')
			return redirect('registration_site:signup')
	else:
	    context = {}
	    context['user_form'] = UserSignupForm()
	    context['panel_title'] = 'Sign up'
	    return render(request, 'registration_site/sign_in.html', context)

def createOrUpdateDjangoUser(email, password, first_name, last_name):
    try:
        user = User.objects.get(username=email)
        user.set_password(password)
    except User.DoesNotExist:
        user = User.objects.create_user(username=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return user


