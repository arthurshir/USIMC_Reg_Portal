from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Hello, world!")

def login(request):
    return HttpResponse("Log in BOIII")