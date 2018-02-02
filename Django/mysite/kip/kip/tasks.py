from __future__ import absolute_import
import os
from celery import Celery, shared_task
from django.conf import settings
import celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kip.settings')
app = Celery('kip')

# Using a string here means the worker will not have to
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


class MyTask(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@shared_task
def add(x, y):
    return x + y


@app.task(base=MyTask, name='multiplication-of-two-numbers')
def multi(x, y):
    return x * y


@app.task(base=MyTask, name='raise key error')
def kerror(x, y):
    raise KeyError()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(bind=True, name='adding-to-number')
def add_test(self, x):
    try:
        total = 0
        # logger.debug('adding to {0}'.format(x))
        for i in range(1, x):
            total += i
        return total
    except Exception as e:
        print(e)
        # return add_test(x)
        # raise self.retry(x)
        raise self.retry(args=[100], exc=e, countdown=2,  max_retries=3)

    # return 100


@app.task(retries=4, default_retry_delay=1)
def fail():
    try:
        assert False
    except Exception as e:
      print 'Try {0}/{1}'.format(fail.request.retries, fail.max_retries)
      # Print log message with current retry
      raise fail.retry(exc=e)
