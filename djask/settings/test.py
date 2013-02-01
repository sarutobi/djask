# coding: utf-8

from .local import *

TEST_DISCOVERY_ROOT = BASE_PATH = SITE_ROOT
TEST_RUNNER = "tests.runner.DiscoveryRunner"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
