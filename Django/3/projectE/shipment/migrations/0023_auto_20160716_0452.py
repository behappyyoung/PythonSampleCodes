# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-16 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0022_auto_20160716_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='date',
            field=models.CharField(default=datetime.date.today, max_length=20),
        ),
    ]
