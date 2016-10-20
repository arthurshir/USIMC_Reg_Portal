"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
