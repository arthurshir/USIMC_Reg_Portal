"""Main Website URL Configuration"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from rest_framework import routers
from rest_framework_jwt.views import(
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

app_name = 'registration_site'

router = routers.SimpleRouter()
router.register(r'users', views.USIMCUserViewSet, 'users-list')
router.register(r'entries', views.EntryList.as_view(), 'entry-list-and-create')
router.register(r'entry', views.EntryDetail.as_view(), 'entry')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token/obtain/', obtain_jwt_token),
    url(r'^api-token/refresh/', refresh_jwt_token),
    url(r'^api-token/verify/', verify_jwt_token),

    url(r'^users/register/$', views.register),
    url(r'^users/login/$', views.login),
    url(r'^entries/list/$', views.EntryList.as_view()),
    url(r'^entries/(?P<pk>[\w\-]+)/$', views.EntryDetail.as_view()),
    url(r'^entries/create/$', views.create_entry),

    # entry/<pid>/
    # entry/<pid>/

]


