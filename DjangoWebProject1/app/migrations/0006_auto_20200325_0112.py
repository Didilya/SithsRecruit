# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200325_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='answersFalseCount',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='answersTrueCount',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='resrutesWhoPass',
            field=models.ManyToManyField(blank=True, to='app.Recrutes'),
        ),
    ]