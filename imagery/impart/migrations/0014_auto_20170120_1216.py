# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0013_content_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='identifier',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]