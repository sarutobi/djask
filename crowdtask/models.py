# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from fields import JSONField


class Application(models.Model):
    '''
    Base application class. Application is a high-level group of tasks,
    that shoul be completed. Application contains all task-related data,
    (i.e. description, logo, author, etc.)
    '''
    name = models.CharField(max_length=100)
    #Common task question
    question = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField()
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    valid_until = models.DateTimeField(blank=True, null=True)
    really_finished = models.DateTimeField(blank=True, null=True)
    user = models. ForeignKey(User)  # only authorized users can create applications
    parallels = models.BooleanField()  # User can solve more than one task in time
    finished = models.BooleanField(editable=False, default=False)
    presenter = JSONField(default='')

    def __unicode__(self):
        return self.name


class Task(models.Model):
    '''
    Simple task description. Each task must be connected to one application.
    '''
    TASK_STATUS = (
        (0, 'Created'),
        (1, 'In progress'),
        (2, 'Pending'),
        (3, 'Valid'),
        (4, 'Invalid'),
        (5, 'Error'),
    )
    application = models.ForeignKey(Application)
    user = models.ForeignKey(User)  #Only authorized users can create tasks
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    valid_until = models.DateTimeField(blank=True, null=True)
    status = models.PositiveIntegerField(choices=TASK_STATUS)
    # Priority - value between 0 (low) and 100 (utmost) - hint for tracker
    priority = models.PositiveIntegerField()
    #Number of answers to complete task
    quorum = models.PositiveIntegerField()
    #Max numbers of task runs
    max_runs = models.PositiveIntegerField(default=20)
    current_runs = models.PositiveIntegerField(default=0, editable=False)
    info = JSONField()


class TaskRun(models.Model):
    '''
    When user solve a task, answer and related information collected here.
    '''
    task = models.ForeignKey(Task)
    application = models.ForeignKey(Application)
    info = JSONField()
    remote_ip = models.IPAddressField()
    user = models.ForeignKey(User, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    accepted = models.BooleanField(default=False)
