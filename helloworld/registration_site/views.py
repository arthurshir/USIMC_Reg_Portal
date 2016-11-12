from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserSigninForm, UserSignupForm, ParentForm, PerformerForm, TeacherForm, PieceForm, PieceFormSetHelper
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms.models import formset_factory
from .models import Performer, Profile, Parent
import json

def index(request):
    return HttpResponse("Hello, world!")

def dashboard(request):
	profile = Profile.objects.get(user = request.user)
	performer = Performer.objects.get(owningProfile = profile)

	if request.method == "POST":
		performerForm = PerformerForm(request.POST, instance=performer, prefix="performer")
		teacherForm = TeacherForm(request.POST, instance=performer._teacher, prefix="teacher")
		pieceForm1 = PieceForm(request.POST, instance=performer.piece1, prefix="piece1")
		pieceForm2 = PieceForm(request.POST, instance=performer.piece2, prefix="piece2")
		chinesePieceForm = PieceForm(request.POST, instance=performer.chinesePiece, prefix="chinesePiece")
		parentForm = ParentForm(request.POST, instance=profile.parent, prefix="parent")

		data = {}
		if performerForm.is_valid() and teacherForm.is_valid() and pieceForm1.is_valid() and pieceForm2.is_valid() and chinesePieceForm.is_valid() and parentForm.is_valid():
			performerForm.save()
			teacherForm.save()
			pieceForm1.save()
			pieceForm2.save()
			chinesePieceForm.save()
			parentForm.save()
			data['success'] = True
			print("Form should be saved")
		else:
			data['success'] = False
			data['error'] = "Invalid Form"
			print("Invalid Form")
		return HttpResponse(json.dumps(data), content_type="application/json")

	else:
		context = {}
		context['performerForm'] = PerformerForm(instance=performer, prefix="performer")
		context['teacherForm'] = TeacherForm(instance=performer._teacher, prefix="teacher")
		context['pieceForm1'] = PieceForm(instance=performer.piece1, prefix="piece1")
		context['pieceForm2'] = PieceForm(instance=performer.piece2, prefix="piece2")
		context['chinesePieceForm'] = PieceForm(instance=performer.chinesePiece, prefix="chinesePiece")

		context['parentForm'] = ParentForm(instance=profile.parent, prefix="parent")
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

			if not '@' in email:
				messages.warning(request, 'Not an email address', extra_tags='signup')
				return redirect('registration_site:signup')

			if User.objects.filter(username=email).exists():
				messages.warning(request, 'A User for {} already exists'.format(email), extra_tags='signup')
				return redirect('registration_site:signup')

			user = createOrUpdateDjangoUser(email, password, first_name, last_name)
			login(request, user)
			parent = Parent.objects.create()
			profile = Profile.objects.create(user = request.user, parent=parent)
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


