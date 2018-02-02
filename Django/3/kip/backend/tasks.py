from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kip.settings')
app = Celery('kip')

# Using a string here means the worker will not have to
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def add(x, y):
    return x + y

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
