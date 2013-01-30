# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from django.test.simple import DjangoTestSuiteRunner, reorder_suite
from django.utils.importlib import import_module
from django.utils.unittest.loader import defaultTestLoader


class DiscoveryRunner(DjangoTestSuiteRunner):
    """A test suite runner using unittest2 discovery."""
    def build_suite(self, test_labels, extra_tests=None,
                    **kwargs):
        suite = None
        discovery_root = settings.TEST_DISCOVERY_ROOT

        if test_labels:
            suite = defaultTestLoader.loadTestsFromNames(
                test_labels)

        if suite is None:
            suite = defaultTestLoader.discover(
                discovery_root,
                top_level_dir=settings.BASE_PATH,
                )

        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)

        return reorder_suite(suite, (TestCase,))
