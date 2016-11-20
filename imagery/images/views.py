from django.shortcuts import render
from imagery.images.models import Imagery

import logging
logger = logging.getLogger("imagery")


def selects(request, page=1):
    """Get all select entries."""

    selects = Imagery.objects.reverse()

    logger.error("Retrieved %s images." % len(selects))

    attributes = {'selects': selects, 'hello': 'there'}

    return render(request, 'pages/select.html', attributes)
