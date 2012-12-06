# -*- coding: utf-8 -*-

import logging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

from crowdtask.models import Application
from crowdtask.forms import ApplicationForm, TaskForm

logger = logging.getLogger(__name__)

def apps_list(request):
    ''' Show all applications '''
    logger.debug("apps list requested from %s" % request.META['REMOTE_ADDR'])
    return TemplateResponse(request, 'apps_list.html',
        { 'apps': Application.objects.all(),
        }
    )

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
    '''User profile view'''
    model = User
    template_name="user_profile.html"

    def get_object(self):
        return self.request.user
