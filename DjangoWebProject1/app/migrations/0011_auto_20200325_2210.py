# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-25 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200325_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='answerTrue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answerWrong',
            field=models.BooleanField(default=False),
        ),
    ]
