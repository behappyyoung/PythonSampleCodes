from __future__ import absolute_import
import os
from celery import Celery, shared_task
from celery.task import task
# from celery.decorators import task
from django.conf import settings
import celery
# from celery.utils.log import get_task_logger
import logging

logger = logging.getLogger(__name__)
print(__name__)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ifshape.settings')
app = Celery('mybackend')

# Using a string here means the worker will not have to
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# logger = get_task_logger(__name__)


class MyTask(celery.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@shared_task
def add(x, y):
    logger.error('log - Adding {0} + {1}'.format(x, y))
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@task(base=MyTask)
def e_add(x, y):
    raise KeyError()


@app.task(base=MyTask, name='multiplication-of-two-numbers')
def multi(x, y):
    return x * y


@app.task(bind=True, name='adding-to-number')
def add_test(self, x):
    try:
        total = 0
        logger.debug('adding to {0}'.format(x))
        for i in range(1, x):
            total += i
        return total
    except Exception as e:
        logger.error('in exception')
        # print(e)
        # return add_test(x)
        # raise self.retry(100)
        print('Try {0}/{1}'.format(self.request.retries, self.max_retries))
        if int(self.request.retries) > 1:
            c_arg = 10000
        else:
            c_arg = x

        raise self.retry(args=[c_arg], exc=e, countdown=10, max_retries=3)


class AddTask(app.Task):
    def run(self, x, y):
        return x+y


@app.task(bind=True, retries=4, default_retry_delay=1)
def fail(self):
    try:
        assert False
    except AssertionError as e:
        logger.error('false')
        print('Try {0}/{1}'.format(self.request.retries, self.max_retries))
        # Print log message with current retry
        raise self.retry(exc=e, countdown=30)
