# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-16 10:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0017_auto_20160715_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=200)),
                ('number', models.CharField(default=' ', max_length=200)),
                ('loadage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='0000', max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('chief', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('manager', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('car', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.cars')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.date.today)),
                ('order_customer', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='shipment.customer')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=200)),
                ('price', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='standard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.standard'),
        ),
        migrations.AddField(
            model_name='orders',
            name='site',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.site'),
        ),
        migrations.AddField(
            model_name='orders',
            name='sub_customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sub_customer', to='shipment.customer'),
        ),
        migrations.AddField(
            model_name='customer',
            name='site',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.site'),
        ),
        migrations.AddField(
            model_name='customer',
            name='standard',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.standard'),
        ),
    ]
