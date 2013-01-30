# -*- coding: utf-8 -*-

import unittest

from crowdtask.models import Task
from .factories import AppFactory, TaskFactory


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.app = AppFactory.build()

    def tearDown(self):
        self.app = None

    def test_application(self):
        '''Application should be created'''
        self.assertNotEqual(None, self.app)

    def test_application_uncode(self):
        '''Application showld show name in representations'''
        self.assertEqual(self.app.name, "%s" % self.app)

    def test_absolute_url(self):
        self.assertEqual('/app/view/%s' % self.app.slug, self.app.get_absolute_url())

    def test_application_name(self):
        '''Application should have name'''
        self.assertEqual(6, len(self.app.name))

    def test_application_slug(self):
        '''Application should get slug'''
        self.assertEqual('slug_%s' % self.app.name, self.app.slug)

    def test_creation_time(self):
        '''Application creation time'''
        self.assertEqual(None, self.app.creation_time)

    def test_append_task(self):
        '''Test append task to application'''
        self.app.save()
        self.assertIsNotNone(self.app.id)
        self.app.append_task(TaskFactory())
        self.assertEqual(1, self.tasks())


class TaskTest(unittest.TestCase):

    def test_task_creation(self):
        task = Task()
        self.assertEqual(0, task.status)
