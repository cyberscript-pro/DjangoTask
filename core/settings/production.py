import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('BD_NAME'),
        'USER': os.getenv('BD_USER'),
        'PASSWORD': os.getenv('BD_PASSWORD'),
        'HOST': os.getenv('BD_HOST'),
        'PORT': os.getenv('BD_PORT'),
    }
}