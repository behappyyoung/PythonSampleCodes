from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

STATUS_CODE = (
    ('A', 'Active'),
    ('I', 'In Active')
)


class WorkflowManager(models.Manager):          # override manager to show only active workflows
    def get_queryset(self):
        return super(WorkflowManager, self).get_queryset().filter(status='A')

class WorkflowType(models.Model):
    type = models.CharField(max_length=20, null=False)
    type_name = models.CharField(max_length=50, null=False)
    desc = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CODE, default='A')
    wf_objects = WorkflowManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.type_name


class Workflows(models.Model):
    type = models.ForeignKey('WorkflowType', default=1)
    name = models.CharField(max_length=100, null=False)
    version = models.CharField(max_length=20, default='1')
    workflow_id = models.CharField(max_length=200, null=False)
    inputs = models.CharField(max_length=400, null=True, blank=True)
    fixed_inputs = models.CharField(max_length=400, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CODE, default='A')
    objects = models.Manager()
    wf_objects = WorkflowManager()

    def __unicode__(self):
        return self.workflow_id


# class LabWorkFlowType(models.Model):
#     type = models.CharField(max_length=20, null=False)
#     type_name = models.CharField(max_length=50, null=False)
#     desc = models.CharField(max_length=200, null=True)
#

class LabWorkFlowStatus(models.Model):
    status = models.CharField(max_length=20, null=False, default='CREATED')
    status_name = models.CharField(max_length=50, null=False, default='new lab work created')
    desc = models.CharField(max_length=200, null=True)


class LabWorkFlows(models.Model):
    # type = models.ForeignKey('LabWorkFlowType', default=1)
    name = models.CharField(max_length=100, null=False)
    created_date = models.CharField(max_length=50, null=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    update_date = models.CharField(max_length=50, null=False, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    type = models.CharField(max_length=100, null=True)
    samples_list = models.CharField(max_length=200, null=True, blank=True)
    status = models.ForeignKey('LabWorkFlowStatus', default=1)
    objects = models.Manager()
    wf_objects = WorkflowManager()

    def __unicode__(self):
        return self.name
