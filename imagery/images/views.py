from django.shortcuts import render
from imagery.images.models import Artist

import logging
logger = logging.getLogger("imagery")


def artists(request, page=1):
    """Get all select entries."""

    artists = Artist.objects.filter(active=True)

    logger.error("Retrieved %s artists." % len(artists))

    attributes = {'artists': artists, 'intro': 'Hello there!'}

    return render(request, 'pages/home.html', attributes)
