"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
