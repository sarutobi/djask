# -*- coding: utf-8 -*-

from django import forms

from crowdtask.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['user', 'really_finished']
