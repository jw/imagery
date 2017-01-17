from django.db import models
from markdownx.models import MarkdownxField


class Dated(models.Model):
    """Base type for all models with associated dates."""
    creation_date = models.DateTimeField('Creation date')
    publication_date = models.DateTimeField('Publication date')
    archive_date = models.DateTimeField('Archive date')


class News(Dated):
    """News topic."""
    location = models.CharField(max_length=1024,
                                help_text="The location where the news took/will take place.")
    header = models.CharField(max_length=256, help_text="The header.")
    body_english = MarkdownxField(max_length=4096, help_text="The news body in English.")
    body_dutch = MarkdownxField(max_length=4096, help_text="The news body in Dutch.")
    active = models.BooleanField(default=True, help_text="If set the news will be shown, otherwise it will not.")
    archived = models.BooleanField(default=False, help_text="If set the news will be part of the archive section.")

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.header


class Manifest(Dated):
    header = models.CharField(max_length=256)
    body_english = MarkdownxField(max_length=4096)
    body_dutch = MarkdownxField(max_length=4096)
    active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False,
                                   help_text="If set the manifest will be part of the archive section.")

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "Manifesti"


class LandPrice(models.Model):
    """
        There are different types of art.  Regarding the type,
        there is a different price.
    """
    PRIZE_TYPE = (
        ('P', 'Painting'),
        ('D', 'Drawing'),
        ('I', 'Photo'),
        ('S', 'Statue'),
        ('M', 'Media')
    )
    type = models.CharField(max_length=1, choices=PRIZE_TYPE, null=False)
    header = models.CharField(max_length=256)
    body_english = MarkdownxField(max_length=4096)
    body_dutch = MarkdownxField(max_length=4069)
    order = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    # TODO: add static method(s) to calculate price

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '%s' % self.header


# TODO: Create Content Model and replace this one with it.
class NameValuePair(models.Model):
    """
        The section contains the sections (like art, or news, or manifesti),
        and the name/value pairs contain the key and the text to be shown in that
        place.  See documentation for the valid section and name/key identifiers.
    """
    section = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    value = MarkdownxField(max_length=4096)

    def __str__(self):
        return '[%s] %s: %s' % (self.section, self.name, self.value)


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
    z = models.IntegerField(blank=True, null=True, help_text='Depth of the piece')
    materials = models.CharField(max_length=512)
    active = models.BooleanField(default=True)
    in_private_collection = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    artist = models.ForeignKey(Artist, blank=True, null=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    bank = models.CharField(max_length=256, blank=True, null=True)
    vat = models.CharField(max_length=256, blank=True, null=True)
    company = models.CharField(max_length=256, blank=True, null=True)
    telephone = models.CharField(max_length=256, blank=True, null=True)
    street = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " <" + self.email + ">"

