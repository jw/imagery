# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0016_auto_20170126_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='markdown',
            field=models.BooleanField(default=False),
        ),
    ]