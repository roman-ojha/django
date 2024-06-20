
from pathlib import Path
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = 'django-insecure-f!jg)ovdn+4&3_5c*(%acul7@guo0_ckfc1zpyasoq@lre61&z'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'logdemo.urls'

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

WSGI_APPLICATION = 'logdemo.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging:
# https://docs.djangoproject.com/en/5.0/topics/logging/#logging-explanation
# https://docs.djangoproject.com/en/5.0/howto/logging/#logging-how-to

# https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # adding formatters
    "formatters": {  # Configure Formatter: https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-formatter
        # adding formatter that we can add it into handlers
        "simple": {
            "format": "{asctime}:{levelname} {message}",
            "style": "{",
        },
        "verbose": {
            "format": "{name} {asctime} {levelname}  - {module}.py (line {lineno:d}) {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {  # Here now we can define any handler
        "console": {
            # 'logging.StreamHandler' is one of the logging handler
            "class": "logging.StreamHandler",
            # "level": "DEBUG",
            "level": env("DJANGO_LOG_LEVEL"),
            # add formatter into handler
            "formatter": "simple",
        },
        # creating the file handler
        "file": {
            # "level": "DEBUG",
            "class": "logging.FileHandler",
            # You should dynamically add these file name or any other dynamic value using environment variables
            # or any other log 'level' dynamically from environment variable
            # Why?:
            # - you ma want to determine this by environment variable
            # - and you my want to setup this based on per server like the name and the location of the files that you want to log output to
            # - for 'level' you may want to see DEBUG logging on development server but on on the production one
            "filename": env("DJANGO_LOG_FILE"),
            "level": env("DJANGO_LOG_LEVEL"),
            # add formatter into handler
            "formatter": "verbose"
        },
        "file_views": {
            "class": "logging.FileHandler",
            "filename": "django_logs.views.log",
            "level": env("DJANGO_LOG_LEVEL"),
            "formatter": "verbose"
        }
    },
    "loggers": {
        # Define any logging objects that you want to use within this django application
        "": {  # this will process records from all loggers, so now all the log out will be send out to this logger
            # https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-logger-mapping
            # "level": "DEBUG",  # level of logging that you want to output
            "level": env("DJANGO_LOG_LEVEL"),
            "handlers": ["file", "console"],
        },

        # Logger namespacing: https://docs.djangoproject.com/en/5.0/howto/logging/#use-logger-namespacing
        # A named logging configuration will capture logs only from loggers with matching names.
        # The namespace of a logger instance is defined using getLogger(). For example in views.py of my_app:
        # logger = logging.getLogger(__name__)
        # "logdemo.views": {
        #     "level": env("DJANGO_LOG_LEVEL"),
        #     "handlers": ["file", "console"],
        # }

        # Logging Hierarchy:
        "logdemo": {  # A logger mapping named 'logdemo' will be more permissive, capturing records from loggers anywhere within the my_app namespace (including logdemo.views, logdemo.utils, and so on):
            "level": env("DJANGO_LOG_LEVEL"),
            "handlers": ["file", "console"],
        },
        "logdemo.views": {
            "level": env("DJANGO_LOG_LEVEL"),
            "handlers": ["file_views"],
            # NOTE: that if 'logdemo.view' have any logging then it will get handled by both 'logdemo.views' & 'logdemo' logger by default but if you want to disable sending logger to parent and just want to output using only this logger then you can disable like this:
            "propagate": False
        }
    },
    # "root": {
    #     # and we can add those handler into root handler
    #     "handlers": ["console"],
    #     # Now this will configure root logger to send messages with warning level or higher to the 'console'
    #     "level": "WARNING",
    # },

    # Log Aggregation Service: It allows to send these logs to an external locations where we can use service specialized for dealing with these logs and analyzing them searching for particular items in the logs and also dashboards and charts:
    # https://betterstack.com/logs
    # Better Stacks aggregate all your logs into structured data you can query like a single database with SQL. Put logs from all your servers, apps, containers, clusters, and cloud providers in one place and search them in real time.
    # https://youtu.be/XSwIUnGXrwY?t=1938
}
