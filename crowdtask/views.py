# -*- coding: utf-8 -*-

import logging

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from crowdtask.models import Application
from crowdtask.forms import ApplicationForm, TaskForm

logger = logging.getLogger(__name__)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class AppsList(ListView):
    '''Show all acive applications'''
    template_name = "apps_list.html"
    context_object_name = "apps"

    def get_queryset(self):
        return Application.objects.filter(finished=False)

def create_user(request):
    ''' register form'''
    if request.method == 'GET':
        return TemplateResponse(request, 'register_form.html',
            {'form': UserCreationForm(), })
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return TemplateResponse(request, 'register_form.html',
            {'form': form,})

def create_app(request):
    '''create app form'''
    if request.method == 'GET':
        return TemplateResponse(request, 'application_form.html',
            {'form': ApplicationForm(), })
    elif request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.user_id = request.user.id
            logger.debug("App data: %s" % app)
            app.save()
            return HttpResponseRedirect('/')
        return TemplateResponse(request, 'application_form.html',
            {'form': form,})

def create_task(request):
    ''' create task form'''
    if request.method == 'GET':
        return TemplateResponse(request, 'application_form.html',
            {'form': TaskForm(),})


class UserProfile(DetailView):
    '''Own user profile view'''
    model = User
    template_name="user_profile.html"

    def get_object(self):
        return self.request.user


class UserApps(ListView):
    '''Self created applications'''
    template_name="user_applications.html"
    context_object_name = 'apps'

    def get_queryset(self):
        return Application.objects.filter(user_id=self.request.user.id)
