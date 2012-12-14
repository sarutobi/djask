# -*- coding: utf-8 -*-

from rest_framework import serializers

from crowdtask.models import Application, Task


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
