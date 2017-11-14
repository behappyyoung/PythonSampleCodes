# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime
from django_mysql.models import JSONField


STATUS_CODE = (
    ('A', 'Active'),
    ('I', 'In Active')
)


class WorkflowManager(models.Manager):          # override manager to show only active workflows
    def get_queryset(self):
        return super(WorkflowManager, self).get_queryset().filter(status='A')


class Workflows(models.Model):
    type = models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=100, null=False)
    version = models.CharField(max_length=20, default='1.0')
    workflow_id = models.CharField(max_length=200, null=False)
    inputs = JSONField(default=dict)
    fixed_inputs = JSONField(default=dict, null=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CODE, default='A')
    objects = models.Manager()
    wf_objects = WorkflowManager()

    def __unicode__(self):
        return self.workflow_id