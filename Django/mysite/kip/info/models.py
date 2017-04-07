# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_mysql.models import JSONField


# Create your models here.
class tag(models.Model):
    name = models.CharField(max_length=50, null=False)
    Url = models.CharField(max_length=500, null=False, default='/')


class menu(models.Model):
    menu_json = JSONField(default=dict)
    parent = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=50, null=False)
    Url = models.CharField(max_length=100, null=False, default='/')

