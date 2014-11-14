from __future__ import absolute_import

from celery import shared_task

from celery.task import periodic_task
from datetime import timedelta

@periodic_task(run_every = timedelta(seconds = 60))
def test():
    print("is works!")

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
