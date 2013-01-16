# -*- coding: utf-8 -*-

from django import forms

from crowdtask.models import Application, Task


class ApplicationForm(forms.ModelForm):
    '''Create application form'''
    class Meta:
        model = Application
        widgets = {"presenter": forms.HiddenInput(),}
        exclude = ['user', 'really_finished']


class TaskForm(forms.ModelForm):
    '''Create task form'''
    class Meta:
        model = Task
        exclude = ['user', 'creation_time', 'status', 'current_runs']
        widgets = {'application': forms.HiddenInput, }
