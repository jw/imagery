# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-28 18:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0019_auto_20170206_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manifest',
            options={'ordering': ['publication_date'], 'verbose_name_plural': 'Manifests'},
        ),
        migrations.AddField(
            model_name='art',
            name='archived',
            field=models.BooleanField(default=False, help_text='If set the art will be part of the archive section.'),
        ),
        migrations.AlterField(
            model_name='dated',
            name='archive_date',
            field=models.DateTimeField(help_text='The date this model needs to be archived.', verbose_name='Archive date'),
        ),
        migrations.AlterField(
            model_name='dated',
            name='creation_date',
            field=models.DateTimeField(help_text='The model creation date.', verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='dated',
            name='publication_date',
            field=models.DateTimeField(help_text='The date this model needs to be shown on screen.', verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='landprice',
            name='body_dutch',
            field=ckeditor.fields.RichTextField(help_text='Some explanation of the landprice in Dutch.', max_length=4069),
        ),
        migrations.AlterField(
            model_name='landprice',
            name='body_english',
            field=ckeditor.fields.RichTextField(help_text='Some explanation of the landprice in English.', max_length=4096),
        ),
        migrations.AlterField(
            model_name='landprice',
            name='header',
            field=models.CharField(help_text='The header of the landprice.', max_length=256),
        ),
        migrations.AlterField(
            model_name='landprice',
            name='type',
            field=models.CharField(choices=[('P', 'Painting'), ('D', 'Drawing'), ('I', 'Photo'), ('S', 'Statue'), ('M', 'Media')], help_text='The different types of art.', max_length=1),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='active',
            field=models.BooleanField(default=True, help_text='If set the manifest will be shown, otherwise it will not.'),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='body_dutch',
            field=ckeditor.fields.RichTextField(help_text='The manifest in Dutch.', max_length=4096),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='body_english',
            field=ckeditor.fields.RichTextField(help_text='The manifest in English.', max_length=4096),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='header',
            field=models.CharField(blank=True, help_text='The header of the manifest can be left empty.', max_length=256, null=True),
        ),
    ]