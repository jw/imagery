from django.db import models
from ckeditor.fields import RichTextField


class Dated(models.Model):
    """Base type for all models with associated dates."""
    creation_date = models.DateTimeField('Creation date', help_text="The model creation date.")
    publication_date = models.DateTimeField('Publication date',
                                            help_text="The date this model needs to be shown on screen.")
    archive_date = models.DateTimeField('Archive date', help_text="The date this model needs to be archived.")


class News(Dated):
    """News topic."""
    location = models.CharField(max_length=1024,
                                help_text="The location where the news took/will take place.")
    header = models.CharField(max_length=256, help_text="The header.")
    body_english = RichTextField(max_length=4096, help_text="The news body in English.")
    body_dutch = RichTextField(max_length=4096, help_text="The news body in Dutch.")
    active = models.BooleanField(default=True, help_text="If set the news will be shown, otherwise it will not.")
    archived = models.BooleanField(default=False, help_text="If set the news will be part of the archive section.")

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "News"

    def __str__(self):
        return self.header


class Manifest(Dated):
    header = models.CharField(max_length=256, null=True, blank=True,
                              help_text="The header of the manifest can be left empty.")
    body_english = RichTextField(max_length=4096, help_text="The manifest in English.")
    body_dutch = RichTextField(max_length=4096, help_text="The manifest in Dutch.")
    active = models.BooleanField(default=True, help_text="If set the manifest will be shown, otherwise it will not.")
    archived = models.BooleanField(default=False,
                                   help_text="If set the manifest will be part of the archive section.")

    class Meta:
        ordering = ['publication_date']
        verbose_name_plural = "Manifests"

    def __str__(self):
        return self.header if self.header else "Manifest from {}.".format(self.creation_date)


class LandPrice(models.Model):
    """
        There are different types of art.  Regarding the type, there is a different price.
    """
    PRIZE_TYPE = (
        ('P', 'Painting'),
        ('D', 'Drawing'),
        ('I', 'Photo'),
        ('S', 'Statue'),
        ('M', 'Media')
    )
    type = models.CharField(max_length=1, choices=PRIZE_TYPE, null=False, help_text="The different types of art.")
    header = models.CharField(max_length=256, help_text="The header of the landprice.")
    body_english = RichTextField(max_length=4096, help_text="Some explanation of the landprice in English.")
    body_dutch = RichTextField(max_length=4069, help_text="Some explanation of the landprice in Dutch.")
    order = models.PositiveSmallIntegerField(help_text="Order of the landprices.")
    active = models.BooleanField(default=True, help_text="If set the landprice will be shown, otherwise it will not.")

    @staticmethod
    def get_price():
        return "n/a"

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.header


class Content(models.Model):
    """The real content as entered by the administrator of the website."""
    CONTENT_SECTION = (
        ('HO', 'Home'),
        ('NE', 'News'),
        ('AR', 'Archive'),
        ('AN', 'News archive'),
        ('AM', 'Manifest archive'),
        ('MA', 'Manifest'),
        ('LP', 'Land Price'),
        ('AA', 'About my art'),
        ('WO', 'Art'),  # WO from Work
        ('CO', 'Contact')
    )
    section = models.CharField(max_length=2, choices=CONTENT_SECTION, null=False, blank=False,
                               help_text="The section this content is part of.")
    CONTENT_LANGUAGE = (
        ('--', 'No language'),
        ('EN', 'English'),
        ('NL', 'Nederlands')
    )
    language = models.CharField(max_length=2, choices=CONTENT_LANGUAGE, null=False, blank=False,
                                help_text="The language this content is in.")
    key = models.CharField(max_length=255, null=False, help_text="The key, as used by the CMS, must be one word.")
    order = models.PositiveSmallIntegerField(help_text="The order of the section and language.")
    identifier = models.CharField(max_length=255, blank=True, help_text="Identifier.")  # TODO: add CONTENT_IDENTIFIER
    value = RichTextField(max_length=4069, help_text="The content itself.")

    class Meta:
        ordering = ['section', 'language', 'order']

    def __str__(self):
        return 'section: {}, language: {}, key: {} ({}): {}'.format(self.get_section_display(),
                                                                    self.get_language_display(),
                                                                    self.key, self.order, self.value)


class Tag(models.Model):
    tag = models.CharField(max_length=255, unique=True, help_text="A tag, can be used by the works of art.")

    def __str__(self):
        return self.tag


class Artist(models.Model):
    """An artist that is part of this site"""
    name = models.CharField(max_length=255, help_text="The name of artist.")
    link = models.CharField(max_length=255, help_text="The link; please leave as is - will be removed.")  # TODO: this should be a slug
    image = models.ImageField(upload_to='artists', help_text="The image of the artist.")
    active = models.BooleanField(default=False, help_text="If set the artist will be shown, otherwise he/she will not.")

    class Meta:
        ordering = ['name', 'link']

    def __str__(self):
        return self.name


class Art(models.Model):
    name = models.CharField(max_length=255, help_text="The name of the work of art.")
    tags = models.ManyToManyField(Tag, blank=True, help_text="The tags related to this work of art.")
    artist = models.ForeignKey(Artist, help_text="The artist.")
    image = models.ImageField(upload_to='art', help_text="The image of the work of art.")
    land_price = models.ForeignKey(LandPrice, help_text="The landprice related with this work of art.")
    x = models.IntegerField(help_text="The number of centimeters on the x-axis.")
    y = models.IntegerField(help_text="The number of centimeters on the y-axis.")
    z = models.IntegerField(blank=True, null=True, help_text='Depth of the piece')
    materials = models.CharField(max_length=512, help_text="The used materials.")
    active = models.BooleanField(default=True, help_text="If set the work of art will be shown, otherwise it will not.")
    in_private_collection = models.BooleanField(default=False,
                                                help_text="Set this when the work is sold, or unavailable.")
    archived = models.BooleanField(default=False, help_text="If set the art will be part of the archive section.")

    def __str__(self):
        return self.name


class Contact(models.Model):
    artist = models.ForeignKey(Artist, help_text="The artist this contact section is part of.")
    email = models.EmailField(help_text="The email address of the artist.")
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
