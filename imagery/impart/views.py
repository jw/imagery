from django.shortcuts import render

from imagery.impart.models import News, LandPrice, Manifesto

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
