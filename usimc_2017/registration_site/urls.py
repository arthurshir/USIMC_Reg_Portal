"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    # Home Page
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Regular Users
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', views.ApplicationListView.as_view(), name='dashboard'),
    url(r'^dashboard/new/', views.NewApplicationView.as_view(), name='new_application'),
    url(r'^dashboard/redirect/(?P<pk>\d+)/edit/$', views.edit_application_redirect, name='edit_application_redirect'),
    url(r'^dashboard/ensemble/(?P<pk>\d+)/edit/$', views.EditEnsembleApplicationView.as_view(), name='edit_ensemble_application'),
    url(r'^dashboard/solo/(?P<pk>\d+)/edit/$', views.EditSoloApplicationView.as_view(), name='edit_solo_application'),
    url(r'^dashboard/performers/', views.EditPerformersView.as_view(), name='edit_performers'),
    url(r'^dashboard/list/', views.ApplicationListView.as_view(), name='application_list'),
    url(r'^dashboard/delete/(?P<pk>\d+)/$', views.DeleteApplicationView.as_view(), name='delete_application'),

    # Admin Users
    url(r'^admin/login/', views.AdminLoginView.as_view(), name='admin_register'),
    url(r'^admin/download-entries/', views.DownloadEntriesView.as_view(), name='download_entries'),
    url(r'^admin/dashboard/', views.DownloadEntriesView.as_view(), name='admin_dashboard'),
]