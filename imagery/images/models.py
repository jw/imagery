from django.db import models

from photologue.models import Photo


class Tag(models.Model):
    """Each image can have zero to n tags."""
    tag = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tag


class Imagery(Photo):
    """The image."""

    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        # ordering = ['name']
        verbose_name_plural = "Images"
