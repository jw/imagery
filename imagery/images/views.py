from django.shortcuts import render
from imagery.images.models import Artist

import logging

logger = logging.getLogger("imagery")


def artists(request, page=1):
    """Get all select entries."""

    artists = Artist.objects.filter(active=True)

    artists_text = " and ".join(str(artist.name) for artist in artists)

    logger.info("Retrieved %s." % artists_text)

    attributes = {'artists': artists,
                  'home_title': 'We are impart',
                  'home_artists': artists_text}

    return render(request, 'pages/home.html', attributes)
