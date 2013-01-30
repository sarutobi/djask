# coding: utf-8

import factory
import random
import string

from django.contrib.auth.models import User
from crowdtask.models import Application, Task

def generate_string(str_len=6):
    return "".join(random.choice(string.ascii_lowercase) for x in xrange(str_len))

def lorem_ipsum(words=40):
    return " ".join(generate_string(str_len=random.randint(3, 7)) for _ in xrange(words))


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    first_name = 'Tester'
    last_name = 'Boy'
    email = factory.LazyAttribute(lambda a:
        '{0}_{1}@example.com'.format(a.first_name, a.last_name).lower())


class AppFactory(factory.Factory):
    FACTORY_FOR = Application

    name = generate_string()
    question = '%s ?' % lorem_ipsum(4)
    description = lorem_ipsum(20)
    slug = factory.LazyAttribute(lambda a: 'slug_{0}'.format(a.name).lower())
    valid_until = None
    user = factory.SubFactory(UserFactory)


class TaskFactory(factory.Factory):
    FACTORY_FOR = Task

    name = generate_string()

def user_generator():
    pass


