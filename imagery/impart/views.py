from django.http import Http404
from django.shortcuts import render

from imagery.impart.models import News, LandPrice, Manifest, Artist, Art, NameValuePair, Contact

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

    logger.info("Showing details of " + artist.name + ".")

    # TODO: update the NameValuePairs to Content
    text = NameValuePair.objects.all()

    works = Art.objects.all()

    contact = Contact.objects.all()

    # TODO: this should not be here!
    prices = LandPrice.objects.filter(active=True)
    works_tags = [p.header for p in prices if p.active]

    attributes = {'text': text,
                  'works': works,
                  'works_tags': works_tags}

    return render(request, 'pages/artist.html', attributes)


def index(request):
    """
    The complete home page. Gets artists, news, mainfesti,
    land prices.
    """

    artists = Artist.objects.filter(active=True)
    artists_text = " and ".join(str(artist.name) for artist in artists)
    logger.info("Retrieved %s." % artists_text)

    news = News.objects.filter(active=True).reverse()

    manifests = Manifest.objects.filter(active=True).reverse()

    prices = LandPrice.objects.filter(active=True)

    # TODO: this needs to go to the artist page
    works = Art.objects.all()
    # TODO: this should not be here!
    works_tags = [p.header for p in prices if p.active]

    attributes = {'artists': artists,
                  'home_title': 'We are impart',
                  'home_artists': artists_text,  # TODO: remove this!
                  'news': news,
                  'manifests': manifests,
                  'prices': prices,
                  'works': works,
                  'works_tags': works_tags}  # TODO: remove this!

    return render(request, 'pages/index.html', attributes)
