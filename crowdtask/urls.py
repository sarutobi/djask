# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from crowdtask.views import UserApps, UpdateApp, AppDetails, CreateTask,\
    AppTasksList, BaseTaskView

urlpatterns = patterns('crowdtask',
    (r'^new$', 'views.create_app'),
    (r'^created$', UserApps.as_view()),
    (r'^edit/(?P<pk>\d+)$', UpdateApp.as_view()),
    url(r'^view/(?P<slug>[a-z]+)$', AppDetails.as_view()),
    (r'^(?P<pk>\d+)/newtask$', CreateTask.as_view()),
    (r'^(?P<slug>[a-z_]+)/tasks$', AppTasksList.as_view()),
    (r'^(?P<slug>[a-z_]+)/showtask$', BaseTaskView.as_view()),
)

