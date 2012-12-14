# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse as django_reverse

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from crowdtask.api.serializers import ApplicationSerializer
from crowdtask.models import Application

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'applications': reverse('apps-list', request=request),
    })


class ApplicationList(generics.ListAPIView):
    model = Application
    serializer_class = ApplicationSerializer
