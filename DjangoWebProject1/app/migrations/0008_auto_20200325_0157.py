# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-24 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200325_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='optionNo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='optionYes',
            field=models.BooleanField(default=True),
        ),
    ]
