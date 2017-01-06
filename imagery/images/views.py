from django.shortcuts import render
from imagery.images.models import Artist

import logging

from imagery.impart.models import NameValuePair

logger = logging.getLogger("imagery")


def artists(request, page=1):
    """Get all select entries."""

    artists = Artist.objects.filter(active=True)

    intro = NameValuePair.objects.filter(section='home').filter(name__startswith='intro')

    logger.info("Retrieved %s artists." % len(artists))

    attributes = {'artists': artists, 'intro': intro}

    return render(request, 'pages/home.html', attributes)
