# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_votes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='votes_name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
