from django.db import models


class Dated(models.Model):
    """Base type for all models with associated dates."""
    creation_date = models.DateTimeField('Creation date')
    publication_date = models.DateTimeField('Publication date')
    archive_date = models.DateTimeField('Archive date')


class News(Dated):
    location = models.CharField(max_length=1024)
    header = models.CharField(max_length=256)
    body_english = models.CharField(max_length=4096)
    body_dutch = models.CharField(max_length=4096)

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.header


class Manifesto(Dated):
    header = models.CharField(max_length=256)
    body_english = models.CharField(max_length=4096)
    body_dutch = models.CharField(max_length=4096)

    class Meta:
        ordering = ['publication_date']


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

    # TODO: add static method(s) to calculate price

    def __str__(self):
        return '%s' % self.header


class NameValuePair(models.Model):
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
