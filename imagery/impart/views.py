from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from imagery.impart.models import News, LandPrice, Manifest, Artist, Art, Content, Contact

import logging
logger = logging.getLogger("imagery")


def archive(request, page=1):

    # FIXME: add filter and order
    news = News.objects.all()

    logger.error("Retrieved %s archive entries." % len(news))

    attributes = {'archives': news}

    return render(request, 'pages/archive.html', attributes)


def artist(request, artist_id):

    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Sorry, but that artist does not exist!")

    # get content...
    about_nl_contents = Content.objects.filter(
        Q(section='AA'), Q(language='NL'), Q(identifier=artist.link)
    )
    about_en_contents = Content.objects.filter(
        Q(section='AA'), Q(language='EN'), Q(identifier=artist.link)
    )
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Sorry, but that artist does not exist!")

    logger.info("Showing details of " + artist.name + ".")

    text = Content.objects.all()

    works = Art.objects.all()

    contact = Contact.objects.all()

    # TODO: this should not be here!
    prices = LandPrice.objects.filter(active=True)
    works_tags = [p.header for p in prices if p.active]

    attributes = {'menu': 'artist',
                  'about_nl_contents': about_nl_contents,
                  'about_en_contents': about_en_contents,
                  'text': text,
                  'works': works,
                  'works_tags': works_tags}

    return render(request, 'pages/artist.html', attributes)


def index(request):
    """The complete home page.

    Gets artists, news, manifests and land prices.
    """

    # get content...
    home_nl_contents = Content.objects.filter(
        Q(section='HO'), Q(language='NL')
    )
    home_en_contents = Content.objects.filter(
        Q(section='HO'), Q(language='EN')
    )

    # ...and all other entities
    artists = Artist.objects.filter(active=True)
    news = News.objects.filter(active=True).reverse()
    manifests = Manifest.objects.filter(active=True).reverse()
    prices = LandPrice.objects.filter(active=True)

    attributes = {'menu': 'home',
                  'home_nl_contents': home_nl_contents,
                  'home_en_contents': home_en_contents,
                  'artists': artists,
                  'news': news,
                  'manifests': manifests,
                  'prices': prices}

    return render(request, 'pages/index.html', attributes)
