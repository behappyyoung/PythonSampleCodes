# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-11 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0009_auto_20160711_0541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='거래처',
            options={'ordering': ['거래처명']},
        ),
        migrations.AlterModelOptions(
            name='출하',
            options={'ordering': ['번호']},
        ),
    ]