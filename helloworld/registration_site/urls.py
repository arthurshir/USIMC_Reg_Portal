"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'registration_site'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.login, name='signup'),
]
