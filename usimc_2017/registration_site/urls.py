"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    # Home Page
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Auth
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^register/', views.RegisterView.as_view(), name='register'),
    url(r'^logout/', views.LogoutView.as_view(), name='logout'),
    # Application Management
    url(r'^dashboard/$', views.ApplicationListView.as_view(), name='dashboard'),
    url(r'^dashboard/new/', views.NewApplicationView.as_view(), name='new_application'),
    url(r'^dashboard/list/', views.ApplicationListView.as_view(), name='application_list'),
    # Application Submission
    url(r'^dashboard/(?P<pk>\d+)/part2/$', views.ApplicationPart2View.as_view(), name='application_part_2'),
    url(r'^dashboard/submission/review/(?P<pk>\d+)/$', views.ReviewSubmissionView.as_view(), name='review_submission'),
    url(r'^dashboard/submission/pay/(?P<pk>\d+)/$', views.PaymentView.as_view(), name='pay'),
    url(r'^dashboard/submission/confirmation/(?P<pk>\d+)/$', views.payment_confirmation, name='payment_confirmation'),
    # Application REST
    url(r'^application/delete/(?P<pk>\d+)/$', views.DeleteApplicationView.as_view(), name='delete_application'),
    url(r'^application/create_pricing_string/$', views.create_pricing_string, name='create_pricing_string'),
    # Application Edit
    url(r'^dashboard/(?P<pk>\d+)/edit/$', views.EditApplicationView.as_view(), name='edit_application'),

    # Admin Users
    url(r'^admin/login/', views.AdminLoginView.as_view(), name='admin_register'),
    url(r'^admin/download-entries/', views.DownloadEntriesView.as_view(), name='download_entries'),
    url(r'^admin/dashboard/', views.DownloadEntriesView.as_view(), name='admin_dashboard'),

    # Info
    url(r'^info/rules.json$', views.rules_json, name='rules_json'),
]