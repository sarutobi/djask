# -*- coding: utf-8 -*-

from datetime import datetime
from rest_framework import serializers

from crowdtask.models import Application, Task


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ('creation_time',)
