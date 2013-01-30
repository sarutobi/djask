# coding: utf-8

import unittest

from .factories import UserFactory


class UserTest(unittest.TestCase):
    '''Test user factory '''

    def setUp(self):
        self.user = UserFactory.build()

    def tearDown(self):
        self.user = None

    def test_user_creation(self):
        self.assertIsNotNone(self.user)
        self.assertEqual('Tester', self.user.first_name)
        self.assertEqual('Boy', self.user.last_name)
        self.assertEqual('tester_boy@example.com', self.user.email)

