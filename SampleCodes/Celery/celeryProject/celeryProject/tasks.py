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
    for i in range(1000000):
        sum += i
    return sum


@app.task
def longcal():
    sum = 0.0
    for i in range(10):
        for j in range(10000000):
            sum += j
    return sum
