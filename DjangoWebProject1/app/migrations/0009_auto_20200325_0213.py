# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-24 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200325_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='optionNo',
            field=models.CharField(default='No', max_length=30),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='optionYes',
            field=models.CharField(default='Yes', max_length=30),
        ),
    ]
