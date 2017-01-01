# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-31 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('images', '0006_auto_20161231_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photologue.Photo'),
            preserve_default=False,
        ),
    ]
