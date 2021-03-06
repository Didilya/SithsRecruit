# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-24 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answerTrue',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='answerWrong',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='resrutesWhoPass',
            field=models.ManyToManyField(to='app.Recrutes'),
        ),
    ]
