# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("impart", "0008_auto_20170117_1518")]

    operations = [
        migrations.AddField(
            model_name="art", name="active", field=models.BooleanField(default=True)
        ),
        migrations.AddField(
            model_name="art",
            name="in_private_collection",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="manifesto",
            name="archived",
            field=models.BooleanField(
                default=False,
                help_text="If set the manifest will be part of the archive section.",
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="archived",
            field=models.BooleanField(
                default=False,
                help_text="If set the news will be part of the archive section.",
            ),
        ),
        migrations.AlterField(
            model_name="landprice",
            name="type",
            field=models.CharField(
                choices=[
                    ("P", "Painting"),
                    ("D", "Drawing"),
                    ("I", "Photo"),
                    ("S", "Statue"),
                    ("M", "Media"),
                ],
                max_length=1,
            ),
        ),
    ]
