# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("impart", "0015_auto_20170120_1632")]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="artist",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="impart.Artist",
            ),
            preserve_default=False,
        )
    ]
