# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0002_jobs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
    ]
