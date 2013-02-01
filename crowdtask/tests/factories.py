# coding: utf-8

import factory
import random
import string

from django.contrib.auth.models import User
from crowdtask.models import Application, Task


def generate_string(str_len=6, src=string.ascii_lowercase):
    return "".join(random.choice(src) for x in xrange(str_len))


def lorem_ipsum(words=40):
    return " ".join(generate_string(str_len=random.randint(3, 7))
                    for _ in xrange(words))


class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = factory.Sequence(lambda n: 'username_%s' % n)
    first_name = generate_string()
    last_name = generate_string()
    email = factory.LazyAttribute(
        lambda a: '{0}@example.com'.
                  format(a.username)
                  .lower())


class AppFactory(factory.Factory):
    FACTORY_FOR = Application

    name = factory.LazyAttribute(lambda a: generate_string())
    question = '%s ?' % lorem_ipsum(4)
    description = lorem_ipsum(20)
    slug = factory.LazyAttribute(lambda a: 'slug_{0}'.format(a.name).lower())
    valid_until = None
    user = factory.SubFactory(UserFactory)


class TaskFactory(factory.Factory):
    FACTORY_FOR = Task

    priority = random.randint(1, 100)
    quorum = random.randint(10, 20)

