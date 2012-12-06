# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from crowdtask.views import UserApps

urlpatterns = patterns('crowdtask',
    (r'^new$', 'views.create_app'),
    (r'created$', UserApps.as_view()),
    (r'^task/new$', 'views.create_task'),
)

