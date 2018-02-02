from __future__ import absolute_import, unicode_literals
from .celery import app
import logging
logger = logging.getLogger(__name__)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def midcal():
    sum = 0
    for i in range(10000):
        sum += i

    return sum


@app.task
def longcal():
    sum = 0
    for i in range(100000000):
        sum += i

    return sum


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
        print('Try {0}/{1}'.format(self.request.retries, self.max_retries))
        if int(self.request.retries) > 1:
            c_arg = 10000
        else:
            c_arg = x

        raise self.retry(args=[c_arg], exc=e, countdown=10, max_retries=3)
