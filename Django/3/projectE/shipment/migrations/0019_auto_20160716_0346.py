# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-16 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0018_auto_20160716_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='0000', max_length=200)),
                ('name', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='customer',
            new_name='customers',
        ),
        migrations.RemoveField(
            model_name='site',
            name='standard',
        ),
        migrations.AddField(
            model_name='standard',
            name='standard_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.standard_name'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='site',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.sites'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='site',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.sites'),
        ),
        migrations.DeleteModel(
            name='site',
        ),
        migrations.AddField(
            model_name='sites',
            name='standard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.standard'),
        ),
    ]
