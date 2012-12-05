# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('crowdtask',
    (r'^new$', 'views.create_app'),
)

