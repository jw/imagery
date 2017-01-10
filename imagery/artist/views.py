from django.shortcuts import render

import logging
logger = logging.getLogger("imagery")


def artist(request):
    """Show an artist page"""

    return render(request, 'pages/index.html')
