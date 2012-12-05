# -*- coding: utf-8 -*-

import logging
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from crowdtask.models import Application

logger = logging.getLogger(__name__)

def apps_list(request):
    ''' Show all applications '''
    logger.debug("apps list requested from %s" % request.META['REMOTE_ADDR'])
    return TemplateResponse(request, 'apps_list.html',
        { 'apps': Application.objects.all(),
        }
    )

def login(request):
    ''' Login form '''
    pass

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
