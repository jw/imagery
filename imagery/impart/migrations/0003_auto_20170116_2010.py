# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0002_auto_20170115_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='z',
            field=models.IntegerField(blank=True, help_text='Depth of the piece', null=True),
        ),
    ]
