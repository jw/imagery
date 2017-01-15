from django.db import models

from imagery.impart.models import Dated, LandPrice


class Tag(models.Model):
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class Artist(models.Model):
    """An artist that is part of this site"""
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='artists')
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', 'link']

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
    artist = models.ForeignKey(Artist)
    image = models.ImageField(upload_to='art')
    land_price = models.ForeignKey(LandPrice)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField(blank=True, help_text='Depth of the piece')
    materials = models.CharField(max_length=512)

    def __str__(self):
        return self.name
