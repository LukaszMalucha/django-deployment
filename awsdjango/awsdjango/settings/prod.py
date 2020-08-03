import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("RDS_DB_NAME"),
        'USER': os.environ.get("RDS_USERNAME"),
        'PASSWORD': os.environ.get("RDS_PASSWORD"),
        'HOST': os.environ.get("RDS_HOSTNAME"),
        'PORT': os.environ.get("RDS_PORT"),
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

AWS_ACCESS_KEY_ID = config()

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

