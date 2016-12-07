from django.db import models

from photologue.models import Photo

from imagery.impart.models import Dated, LandPrice


class Tag(models.Model):
    """Each image can have zero to n tags."""
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class Imagery(Photo):
    """The image."""

    tags = models.ManyToManyField(Tag, blank=True)
    active = models.BooleanField(default=False)
    land_price = models.ForeignKey(LandPrice, on_delete=models.PROTECT)

    class Meta:
        # ordering = ['name']
        verbose_name_plural = "Images"
