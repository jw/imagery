# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 20:33
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [("impart", "0017_content_markdown")]

    operations = [
        migrations.RemoveField(model_name="content", name="markdown"),
        migrations.AlterField(
            model_name="content",
            name="value",
            field=markdownx.models.MarkdownxField(max_length=4069),
        ),
    ]
