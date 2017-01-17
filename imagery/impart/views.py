from django.shortcuts import render

from imagery.impart.models import News, LandPrice, Manifesto, Artist, Art

import logging
logger = logging.getLogger("imagery")


def archive(request, page=1):

    # FIXME: add filter and order
    news = News.objects.all()

    logger.error("Retrieved %s archive entries." % len(news))

    attributes = {'archives': news}

    return render(request, 'pages/archive.html', attributes)


def index(request):
    """
    The complete home page. Gets artists, news, mainfesti,
    land prices.
    """

    artists = Artist.objects.filter(active=True)
    artists_text = " and ".join(str(artist.name) for artist in artists)
    logger.info("Retrieved %s." % artists_text)

    news = News.objects.filter(active=True).reverse()

    manifesti = Manifesto.objects.filter(active=True).reverse()

    prices = LandPrice.objects.filter(active=True)

    # TODO: this needs to go to the artist page
    works = Art.objects.all()
    # TODO: this should not be here!
    works_tags = [p.header for p in prices if p.active]

    attributes = {'artists': artists,
                  'home_title': 'We are impart',
                  'home_artists': artists_text,
                  'news': news,
                  'manifesti': manifesti,
                  'prices': prices,
                  'works': works,
                  'works_tags': works_tags}

    return render(request, 'pages/index.html', attributes)
