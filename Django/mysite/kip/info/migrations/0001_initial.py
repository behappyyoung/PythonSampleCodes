# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-07 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Url', models.CharField(default='/', max_length=500)),
            ],
        ),
    ]
