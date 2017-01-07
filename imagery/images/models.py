from django.db import models

from s3direct.fields import S3DirectField

from imagery.impart.models import Dated, LandPrice


class Tag(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class Artist(models.Model):
    """An artist that is part of this site"""
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = S3DirectField(dest='artists')
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', 'link']

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    artist = models.ForeignKey(Artist)
    image = S3DirectField(dest='art')
    land_price = models.ForeignKey(LandPrice)

    def __str__(self):
        return self.name
