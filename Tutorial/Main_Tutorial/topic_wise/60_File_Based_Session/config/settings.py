from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-571rzejwena05e=m2)*xfverj)zj7yp)lf)02_qmo$0ipf6=g-'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
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

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

#  we will check the timezone to this location just to check session settings
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# overriding the default Session settings:

# default age of the cookie if we didn't set the age
SESSION_COOKIE_AGE = 400

# Change the name of the default Session Cookie name
# default name 'sessionid'
SESSION_COOKIE_NAME = 'session_id'

# Change cookie default path
SESSION_COOKIE_PATH = '/home'

# Change default HTTP Only
# True: it will not given permission to access the cookie from the client site javascript
SESSION_COOKIE_HTTPONLY = True

# Change default Cookie secure, by default it is false
SESSION_COOKIE_SECURE = True

# Change the default session storage
# set file based session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'

# Expire the session on browser close
# default: False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# set the default pat where you want to store session on file based session
SESSION_FILE_PATH = ''

# if you want session to get save in every request
SESSION_SAVE_EVERY_REQUEST = True
