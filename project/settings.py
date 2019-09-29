import os
import django_heroku

# import socket

#######################################################################################################
## For Production and development configuration
# if socket.gethostname().startswith('live'):
#     DJANGO_HOST = "production"
# # Else if host name starts with 'test', set DJANGO_HOST = "test"
# elif socket.gethostname().startswith('test'):
#     DJANGO_HOST = "testing"
# else:
#     # If host doesn't match, assume it's a development server, set DJANGO_HOST = "development"
#     DJANGO_HOST = "development"
#######################################################################################################
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9@9-l!r@%)^uyg0jppqvmd^cro0f=(xv6dy-w8l9e*b8=sk+=u'

# SECURITY WARNING: don't run with debug turned on in production!
# if DJANGO_HOST == "production":
# DEBUG = False
# else:
#     DEBUG = True

# DEBUG = os.environ.get('DJANGO_DEBUG') != 'False'
# or
DEBUG = os.environ.get('DJANGO_DEBUG') is not False

# DEBUG = False

# ALLOWED_HOSTS = ['blog-medium.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'blog-medium.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'myapp.apps.MyappConfig',
    'markdown_deux',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # social Oauth
                'social_django.context_processors.login_redirect',  # social Oauth
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication

    # 'social_core.backends.github.GithubOAuth2',  # for Github authentication
    # 'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# if DJANGO_HOST == "production":
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # driver to connect mongoDB
        'NAME': 'bmedium',
        'HOST': 'mongodb://purveshmakode:admin123@ds033125.mlab.com:33125/bmedium?retryWrites=false',
        'USER': 'purveshmakode',
        'PASSWORD': 'admin123',
    }
}

# else:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'

LOGIN_URL = 'login'

# email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_APP_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_APP_PASS')
# google a/c app pass goes up here


# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # CLient Key
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''  # Secret Key


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_OAUTH_SECRET_KEY')
#
django_heroku.settings(locals())
