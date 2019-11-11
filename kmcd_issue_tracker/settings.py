"""
Django settings for kmcd_issue_tracker project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k)z4c5)z%^w+tj-vlt*fu-=5y#6hsj+3ie0e%ebvr090qwe=z3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Lines added for kmcd-issue-tracking-project
# The C9_HOSTNAME wasn't working in settings.py as an ALLOWED_HOST. So, after a 
# chat with a tutor I set up AWSC9_HOST as an environment variable 
# in .bashrc and am using it in settings.py so that I have an environment variable
# rather than a hardcoded url

ALLOWED_HOSTS = [os.environ.get('AWSC9_HOST')]


# Application definition
# Lines added for kmcd-issue-tracking-project:
# 'django_forms_bootstrap', 'accounts'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap', 
    'accounts',
    'app1_home',
    'app2_user_home',
    'app3_issue_logging',
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

ROOT_URLCONF = 'kmcd_issue_tracker.urls'

# Line added to TEMPLATES for kmcd-issue-tracking-project:
# 'DIRS': [os.path.join(BASE_DIR, 'templates')], This is because there is more 
# than one 'templates' dir and this specifies that all of them could 
# potentially contain templates. This allows us to keep templates separate
# within each app.)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kmcd_issue_tracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Lines added for kmcd-issue-tracking-project
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Lines added for kmcd-issue-tracking-project

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Lines added for kmcd-issue-tracking-project

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# To send a real email:
# TLS = Form of email encryption which is used by gmail

EMAIL_USE_TLS = True

# smtp = Protocol used to send emails

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587


