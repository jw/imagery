# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 15:18
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0007_auto_20170117_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landprice',
            name='body_dutch',
            field=markdownx.models.MarkdownxField(max_length=4069),
        ),
        migrations.AlterField(
            model_name='landprice',
            name='body_english',
            field=markdownx.models.MarkdownxField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='body_dutch',
            field=markdownx.models.MarkdownxField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='manifesto',
            name='body_english',
            field=markdownx.models.MarkdownxField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='namevaluepair',
            name='value',
            field=markdownx.models.MarkdownxField(max_length=4096),
        ),
    ]