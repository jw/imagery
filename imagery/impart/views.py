from django.shortcuts import render

from imagery.impart.models import News, LandPrice, Manifesto, Artist, Art

import logging
logger = logging.getLogger("imagery")


def news(request, page=1):
    """Show the news entries."""

    # FIXME: add datetime and order
    news = News.objects.all()

    logger.error("Retrieved %s news entries." % len(news))

    attributes = {'news': news}

    return render(request, 'pages/news.html', attributes)


def archive(request, page=1):

    # FIXME: add filter and order
    news = News.objects.all()

    logger.error("Retrieved %s archive entries." % len(news))

    attributes = {'archives': news}

    return render(request, 'pages/archive.html', attributes)


def manifest(request):

    manifestos = Manifesto.objects.all()

    logger.info("Retrieved %s manifestos." % len(manifestos))

    attributes = {'manifestos': manifestos}

    return render(request, 'pages/manifest.html', attributes)


def landprice(request):

    prices = LandPrice.objects.all()

    attributes = {'prices': prices}

    return render(request, 'pages/landprice.html', attributes)


def index(request):
    """The complete home page."""

    artists = Artist.objects.filter(active=True)
    artists_text = " and ".join(str(artist.name) for artist in artists)
    logger.info("Retrieved %s." % artists_text)

    news = News.objects.filter(active=True).reverse()

    manifesti = Manifesto.objects.filter(active=True).reverse()

    prices = LandPrice.objects.filter(active=True)

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
