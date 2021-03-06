"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns2 = [
    
    # Admin
    url(r'^admin/', admin.site.urls),

    # Registration
    url(r'', include('registration_site.urls')),

    # Password Recovery
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='user_management/usimc_password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='user_management/usimc_password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='user_management/usimc_password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='user_management/usimc_password_reset_complete.html'), name='password_reset_complete'),

] + static(settings.STATIC_URL_WITHOUT_URI, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r'^registration/', include(urlpatterns2)),
]

handler500 = 'registration_site.views.error_500_view'