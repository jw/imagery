from django.db import models


class Dated(models.Model):
    """Base type for all models with associated dates."""
    creation_date = models.DateTimeField('Creation date')
    publication_date = models.DateTimeField('Publication date')
    archive_date = models.DateTimeField('Archive date')


class News(Dated):
    """News topic"""
    location = models.CharField(max_length=1024,
                                help_text="The location where the news took/will take place.")
    header = models.CharField(max_length=256, help_text="The header.")
    body_english = models.CharField(max_length=4096, help_text="The news body in English.")
    body_dutch = models.CharField(max_length=4096, help_text="The news body in Dutch.")
    active = models.BooleanField(default=True, help_text="If set the news will be shown, otherwise it will not.")

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.header


class Manifesto(Dated):
    header = models.CharField(max_length=256)
    body_english = models.CharField(max_length=4096)
    body_dutch = models.CharField(max_length=4096)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "Manifesti"


class LandPrice(models.Model):
    """
        There are different types of art.  Regarding the type,
        there is a different price.
    """
    PRIZE_TYPE = (
        ('N', 'None'),
        ('I', 'Photo'),
        ('D', 'Drawing'),
        ('P', 'Painting'),
        ('S', 'Statue'),
        ('M', 'Media')
    )
    type = models.CharField(max_length=1, choices=PRIZE_TYPE, null=False)
    header = models.CharField(max_length=256)
    body_english = models.CharField(max_length=4096)
    body_dutch = models.CharField(max_length=4069)
    active = models.BooleanField(default=True)

    # TODO: add static method(s) to calculate price

    def __str__(self):
        return '%s' % self.header


class NameValuePair(models.Model):
    """
        The section contains the sections (like art, or news, or manifesti),
        and the name/value pairs contain the key and the text to be shown in that
        place.  See documentation for the valid section and name/key identifiers.
    """
    section = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    value = models.CharField(max_length=4096)

    def __str__(self):
        return '[%s] %s: %s' % (self.section, self.name, self.value)


class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    bank = models.CharField(max_length=256)
    vat = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    telephone = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)


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

    def __str__(self):
        return self.name
