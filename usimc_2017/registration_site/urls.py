"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^dashboard/new/', views.NewApplicationView.as_view(), name='new_application'),
    url(r'^dashboard/edit/', views.EditApplicationView.as_view(), name='edit_application'),
    url(r'^dashboard/performers/', views.EditPerformersView.as_view(), name='edit_performers'),
    url(r'^dashboard/list/', views.ApplicationListView.as_view(), name='application_list'),
]
