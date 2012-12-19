# -*- coding: utf-8 -*-

from datetime import datetime
from django.core.urlresolvers import reverse as django_reverse

from rest_framework import generics, status
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


class AppCreate(generics.CreateAPIView):
    model = Application
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        data = request.DATA.copy()
        data.__setitem__('user', request.user.id)
        data.__setitem__('creation_time', datetime.now())
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

