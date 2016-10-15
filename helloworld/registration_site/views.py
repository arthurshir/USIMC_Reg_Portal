from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserSigninForm

def index(request):
    return HttpResponse("Hello, world!")

def login(request):
    context = {}
    context['user_form'] = UserSigninForm()
    return render(request, 'registration_site/sign_in.html', context)