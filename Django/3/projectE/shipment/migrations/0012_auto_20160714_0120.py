# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-14 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0011_수주'),
    ]

    operations = [
        migrations.CreateModel(
            name='규격',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('단가', models.IntegerField()),
                ('운반비', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='차량',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('차량번호', models.CharField(default=' ', max_length=200)),
                ('기사이름', models.CharField(default=' ', max_length=200)),
                ('기사연락처', models.CharField(default=' ', max_length=200)),
                ('적재량', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='거래처',
            old_name='연락처1',
            new_name='담당자',
        ),
        migrations.RenameField(
            model_name='거래처',
            old_name='연락처2',
            new_name='전화',
        ),
        migrations.RenameField(
            model_name='거래처',
            old_name='연락처3',
            new_name='팩스',
        ),
        migrations.AddField(
            model_name='거래처',
            name='규격',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.규격'),
        ),
        migrations.AddField(
            model_name='거래처',
            name='차량',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.차량'),
        ),
        migrations.AddField(
            model_name='현장',
            name='규격',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shipment.규격'),
        ),
    ]
