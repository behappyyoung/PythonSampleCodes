# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-17 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0025_auto_20160717_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='site',
        ),
        migrations.AddField(
            model_name='customers',
            name='sites',
            field=models.CharField(default=' ', max_length=400),
        ),
    ]
