"""
Django settings for usimc project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys

import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load Environment variables
dotenv.load_dotenv( os.path.join(BASE_DIR, '.env'))

print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '123456')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['localhost', '54.193.10.208', '127.0.0.1', 'usimc2017registration']

print("DEBUG=", "True" if DEBUG else "False")

# Security
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'registration_site',
    'crispy_forms',
    'django_excel',
    'phonenumber_field',
    'dbbackup',  # django-dbbackup
    'django_crontab',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'usimc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'usimc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'usimc'),
        'USER': os.environ.get('DATABASE_USER', 'usimc'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', '1234'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': '5432',
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# File upload
MAX_UPLOAD_SIZE = 3000000
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN', 'invalid' )
DROPBOX_ROOT_PATH = 'usimc_2019'

# Backups
DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': os.environ.get('DROPBOX_ACCESS_TOKEN', 'invalid' )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# User Management

LOGIN_URL = '/login/'

# CrispyForms
# http://django-crispy-forms.readthedocs.io/en/latest/install.html

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_USER', 'invalid' )
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'invalid' )
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_USER', 'invalid' )
ENABLE_EMAILS_FOR_DEBUG = False


# CRON JOBS
CRONJOBS = [
    ('0 * * * *', 'registration_site.cron.backup_database')
]

# Enable this for Nginx reverse proxy
USE_X_FORWARDED_HOST = True

# Stripe
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY', '123456')
STRIPE_TEST_PUBLISHABLE_KEY = os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY', '123456')
STRIPE_LIVE_SECRET_KEY = os.environ.get('STRIPE_LIVE_SECRET_KEY', '123456')
STRIPE_LIVE_PUBLISHABLE_KEY = os.environ.get('STRIPE_LIVE_PUBLISHABLE_KEY', '123456')

# Competition Status
COMPETITION_ENDED = os.environ.get('COMPETITION_ENDED', 'False') == 'True'
print("Competition_ended = {}".format(COMPETITION_ENDED))
