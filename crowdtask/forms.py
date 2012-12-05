# -*- coding: utf-8 -*-

from django import forms

from crowdtask.models import Application, Task


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ['user', 'really_finished']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', 'creation_time', 'status', 'current_runs']
        widgets = {'application': forms.HiddenInput(), }
