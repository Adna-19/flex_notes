from pathlib import Path
import os
from decouple import config
from django.http.request import host_validation_re

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

CUSTOM_APPS = [
  'accounts.apps.AccountsConfig',
  'notes.apps.NotesConfig',
  'blog.apps.BlogConfig',
]

BUILTIN_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
]

THIRD_PARTY_APPS = [
  'ckeditor',
  'ckeditor_uploader',
  'bootstrap_modal_forms',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'allauth.socialaccount.providers.google',
  'dbbackup',
  'django_cron',
  'taggit',
]

INSTALLED_APPS = CUSTOM_APPS + BUILTIN_APPS + THIRD_PARTY_APPS

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, 'backup')}

CRON_CLASSES = [
    "notes.cron.MyCronJob",
    # ...
]

CKEDITOR_CONFIGS = {

    'simple':{
      'skin': 'moono-lisa',
      'toolbar': 'Custom',
      'toolbar_Custom': [
          ['Bold'],
          ['NumberedList', 'BulletedList'],
      ],

      'width': 690
    
    },

    'moderate':{
      'skin': 'moono-lisa',
      'toolbar': 'Custom',
      'toolbar_Custom': [
          ['Bold', 'Italic'],
          ['Table', 'HorizontalRule'],
          ['TextColor', 'BGColor'],
          ['NumberedList', 'BulletedList'],
          ['Indent', 'Outdent'],
          ['Maximize'],
      ],
      'width': 690,
      'height': 490
    },


    'default': {
        'skin': 'moono-lisa',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
            ['JustifyLeft', 'HorizontalRule' ,'JustifyCenter','JustifyRight','JustifyBlock'],
            ['NumberedList','BulletedList'],
            ['Indent','Outdent'],
            ['Maximize'],
        ],
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'uploadimage',
                'uploadwidget',
                'autoembed',
                'clipboard',
                'uicolor',
                'stylesheetparser',
                'tabletools',
                'templates',
                'exportpdf'
            ]
        ),
        'codeSnippet_theme': 'monokai_sublime',
        'height': 390,
        'width': 690,
    },

    'my_ckeditor': {
        'toolbar': 'Basic',
    }
}

CKEDITOR_RESTRICT_BY_USER = True

LOGIN_REDIRECT_URL = '/notes/dashboard/'

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authentication.EmailAuthBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = "accounts.Account"

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notes_taking_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'notes.context_processors.get_all_notes_type',
                'notes.context_processors.get_url_name',
            ],
        },
    },
]

WSGI_APPLICATION = 'notes_taking_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_builtin')
MEDIA_ROOT = os.path.join(BASE_DIR, "static/media/")

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static')
]

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'

CKEDITOR_UPLOAD_PATH = 'uploads/'

OPEN_WEATHER_API_KEY = config('OPEN_WEATHER_API_KEY')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nimra.rahim99@gmail.com'
EMAIL_HOST_PASSWORD = 'namrarahim1738'
