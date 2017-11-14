# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime
from django_mysql.models import JSONField


class WorkflowManager(models.Manager):          # override manager to show only active workflows
    def get_queryset(self):
        return super(WorkflowManager, self).get_queryset().filter(status='A')

