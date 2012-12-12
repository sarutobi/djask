# -*- coding: utf-8 -*-

import logging

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

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


class CreateUser(CreateView):
    '''Register form'''
    form_class = UserCreationForm
    template_name = "register_form.html"
    success_url = "/"

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


class CreateTask(CreateView):
    form_class = TaskForm
    template_name = "application_form.html"
    success_url = "/apps/created"

    def get(self, request, *args, **kwargs):
        self.app_id = kwargs.get('pk')
        return super(CreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print kwargs.get('pk')
        return super(CreateView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateTask, self).get_form_kwargs()
        #kwargs['application'] = self.pk
        #print self.app_id
        return kwargs

class UpdateApp(UpdateView):
    ''' Update application data view'''
    model = Application
    form_class = ApplicationForm
    template_name = "application_form.html"
    success_url = "/apps/created"


class AppDetails(DetailView):
    '''Application details view'''
    model = Application
    template_name = "application_details.html"
    context_object_name = "app"

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
