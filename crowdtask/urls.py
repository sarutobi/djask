# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from crowdtask.views import UserApps, UpdateApp, AppDetails

urlpatterns = patterns('crowdtask',
    (r'^new$', 'views.create_app'),
    (r'^created$', UserApps.as_view()),
    (r'^edit/(?P<pk>\d+)$', UpdateApp.as_view()),
    (r'^view/(?P<slug>[a-z]+)$', AppDetails.as_view()),
    (r'^task/new$', 'views.create_task'),
)

