from django.shortcuts import render
from imagery.images.models import Artist, Art

import logging

from imagery.impart.models import News, Manifesto, LandPrice

logger = logging.getLogger("imagery")


# TODO: rename this to index/home
# TODO: move this to impart
def artists(request):
    """Get all select artists."""

    artists = Artist.objects.filter(active=True)
    artists_text = " and ".join(str(artist.name) for artist in artists)
    logger.info("Retrieved %s." % artists_text)

    news = News.objects.filter(active=True).reverse()

    manifesti = Manifesto.objects.filter(active=True).reverse()

    prices = LandPrice.objects.all()

    works = Art.objects.all()
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
