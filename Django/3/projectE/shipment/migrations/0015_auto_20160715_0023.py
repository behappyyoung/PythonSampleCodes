# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-15 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0014_규격명'),
    ]

    operations = [
        migrations.AddField(
            model_name='규격명',
            name='m10',
            field=models.CharField(default='10mm', max_length=200),
        ),
        migrations.AddField(
            model_name='규격명',
            name='sb1',
            field=models.CharField(default='SB-1', max_length=200),
        ),
        migrations.AddField(
            model_name='규격명',
            name='sb2',
            field=models.CharField(default='SB-2', max_length=200),
        ),
        migrations.AddField(
            model_name='규격명',
            name='석분',
            field=models.CharField(default='석분', max_length=200),
        ),
    ]
