# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141120_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes_name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
