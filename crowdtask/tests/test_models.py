# -*- coding: utf-8 -*-

import unittest

from crowdtask.models import Task
from .factories import UserFactory, AppFactory, TaskFactory


class UserFactoryTest(unittest.TestCase):
    def setUp(self):
        self.user1 = UserFactory()
        self.user2 = UserFactory()

    def tearDown(self):
        self.user1.delete()
        self.user2.delete()

    def test_user_creation(self):
        self.assertIsNotNone(self.user1)
        self.assertIsNotNone(self.user1.username)

    def test_uniq_users(self):
        self.assertNotEqual(self.user1.username, self.user2.username)


class UserTest(unittest.TestCase):
    '''Test user factory '''

    def setUp(self):
        self.user = UserFactory.build()

    def tearDown(self):
        self.user = None

    def test_user_creation(self):
        self.assertIsNotNone(self.user)
        self.assertEqual(6, len(self.user.first_name))
        self.assertEqual(6, len(self.user.last_name))
        self.assertEqual('%s@example.com' % (self.user.username),
                         self.user.email)



class ApplicationTest(unittest.TestCase):

    def setUp(self):
        user = UserFactory()
        self.app = AppFactory.build()
        self.app.user = user

    def tearDown(self):
        self.app.user.delete()
        self.app = None

    def test_application(self):
        '''Application should be created'''
        self.assertIsNotNone(self.app)
        self.assertNotEqual(False, self.app.user.id)

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


class TestTasksWork(unittest.TestCase):
    def setUp(self):
        user = UserFactory()
        self.task = TaskFactory.build(user=user)

    def tearDown(self):
        self.task.user.delete()
        #self.task.delete()
        self.task = None

    def test_append_task(self):
        '''Test append task to application'''
        app = AppFactory(user=UserFactory())
        app.append_task(TaskFactory.build())
        self.assertEqual(1, len(app.tasks()))


class TaskTest(unittest.TestCase):

    def test_task_creation(self):
        task = Task()
        self.assertEqual(0, task.status)
