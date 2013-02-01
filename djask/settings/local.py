# coding: utf-8

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djask',
        'USER': 'djask',
        'PASSWORD': 'djask',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
