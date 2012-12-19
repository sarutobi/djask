from django.conf.urls import patterns, include, url

from crowdtask.api.views import ApplicationList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    (r'^$', 'crowdtask.api.views.api_root'),
    url(r'^applications$', ApplicationList.as_view(), name='apps-list'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
