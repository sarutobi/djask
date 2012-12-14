from django.conf.urls import patterns, include, url

from crowdtask.api.views import ApplicationList

urlpatterns = patterns('',
    (r'^$', 'crowdtask.api.views.api_root'),
    url(r'^applications$', ApplicationList.as_view(), name='apps-list'),
)

