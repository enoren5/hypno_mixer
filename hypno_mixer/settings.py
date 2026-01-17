import os
# import django_heroku
from decouple import config
import dj_database_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config('DEBUG', default=True, cast=bool)

if os.environ.get('DEBUG', '') != 'False':
    # These are testing settings:
    DEBUG = True # local + staging
    SECURE_HSTS_SECONDS = 0
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_PRELOAD = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
else:
    # These are prod settings:
    DEBUG = False # Set to `False` for prod when done testing (for when the project is finally Live)
    SECURE_HSTS_SECONDS = 7200
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    
    'contents.apps.ContentsConfig',
    # 'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'variables_question.apps.AuthToggleConfig',
    "gateway_defender",
    "widget_tweaks",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hypno_mixer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'variables_question.context_processors.auth_vars',
            ],
        },
    },
]

WSGI_APPLICATION = 'hypno_mixer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_URL = '/home'
LOGIN_REDIRECT_URL = '/'


'''
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "hypno_mixer/static"
'''

'''
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(BASE_DIR.joinpath("hypno_mixer/static"))]
STATIC_ROOT = str(BASE_DIR.joinpath("static"))
'''

'''
Commented out this (Originally from John Elder):
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
Accoding to: https://stackoverflow.com/a/66661021/6095646
Trying this instead : 
'''


STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static') ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# I got the below from:
# https://stackoverflow.com/questions/53859972/django-whitenoise-500-server-error-in-non-debug-mode
''' 
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage" 
'''

# django_heroku.settings(locals())
# Below was suggested here : https://stackoverflow.com/a/52314952/6095646 
DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

DATABASES['default']['CONN_MAX_AGE'] = 0


ADMIN_PATH = os.environ.get('ADMIN_PATH')+'/' if 'ADMIN_PATH' in os.environ else 'admin/'
#CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

'''
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

'''