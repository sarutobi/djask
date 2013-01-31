# coding: utf-8

from .local import *

INSTALLED_APPS += (
    'debug_toolbar',
)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1')

