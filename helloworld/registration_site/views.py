from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserSigninForm, UserSignupForm, ParentForm, PerformerForm, TeacherForm, PieceForm, ChinesePieceForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms.models import formset_factory
from .models import Performer, Profile, Parent, Teacher, Piece, ChinesePiece
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
        chinesePieceForm = ChinesePieceForm(request.POST, instance=performer.chinesePiece, prefix="chinesePiece")
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
            data['error'] = "Invalid Form:\n performerForm: {}\nteacherForm: {}\npieceForm1: {}\npieceForm2: {}\nchinesePieceForm: {}\nparentForm: {}\n".format(performerForm.errors,teacherForm.errors,pieceForm1.errors,pieceForm2.errors,chinesePieceForm.errors,parentForm.errors)
            
        return HttpResponse(json.dumps(data), content_type="application/json")

    else:
        context = {}
        context['performerForm'] = PerformerForm(instance=performer, prefix="performer")
        context['teacherForm'] = TeacherForm(instance=performer._teacher, prefix="teacher")
        context['pieceForm1'] = PieceForm(instance=performer.piece1, prefix="piece1")
        context['pieceForm2'] = PieceForm(instance=performer.piece2, prefix="piece2")
        context['chinesePieceForm'] = ChinesePieceForm(instance=performer.chinesePiece, prefix="chinesePiece")

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
            confirm_password = request.POST.get('confirm_password', '')

            if not '@' in email:
                messages.warning(request, 'Not an email address', extra_tags='signup')
                return redirect('registration_site:signup')

            if User.objects.filter(username=email).exists():
                messages.warning(request, 'A User for {} already exists'.format(email), extra_tags='signup')
                return redirect('registration_site:signup')

            if password != confirm_password: 
                messages.warning(request, 'Passwords do not match', extra_tags='signup')
                return redirect('registration_site:signup')

            ## Instantiate Initial User Objects
            # Profile
            user = createOrUpdateDjangoUser(email, password, first_name, last_name)
            parent = Parent.objects.create()
            profile = Profile.objects.create(user = user, parent=parent)
            # Performer
            teacher = Teacher.objects.create()
            piece1 = Piece.objects.create()
            piece2 = Piece.objects.create()
            chinesePiece = ChinesePiece.objects.create()
            performer = Performer.objects.create(_teacher=teacher, piece1=piece1, piece2=piece2, chinesePiece=chinesePiece, owningProfile=profile)

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


