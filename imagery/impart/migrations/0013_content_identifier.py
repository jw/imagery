# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("impart", "0012_auto_20170120_1203")]

    operations = [
        migrations.AddField(
            model_name="content",
            name="identifier",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        )
    ]
