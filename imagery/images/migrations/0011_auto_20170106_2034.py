# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 20:34
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20170106_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=s3direct.fields.S3DirectField(),
        ),
    ]
