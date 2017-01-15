# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='art')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('z', models.IntegerField(blank=True, help_text='Depth of the piece')),
                ('materials', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='artists')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name', 'link'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impart.Artist'),
        ),
        migrations.AddField(
            model_name='art',
            name='land_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impart.LandPrice'),
        ),
        migrations.AddField(
            model_name='art',
            name='tags',
            field=models.ManyToManyField(blank=True, to='impart.Tag'),
        ),
    ]