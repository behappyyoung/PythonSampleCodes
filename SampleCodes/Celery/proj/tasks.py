from __future__ import absolute_import, unicode_literals
from .celery import app


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
    for i in xrange(10000):
        sum += i

    return sum

@app.task
def longcal():
    sum = 0
    for i in xrange(100000000):
	sum += i

    return sum
