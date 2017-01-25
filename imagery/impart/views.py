from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from imagery.impart.models import News, LandPrice, Manifest, Artist, Art, Content, Contact

import logging
logger = logging.getLogger("imagery")


def archive(request, page=1):
    """Show news and manifest archives."""

    news = News.objects.filter(archived=True)
    manifests = Manifest.objects.filter(archived=True)

    logger.error("Retrieved {} archived news entries, and {} archived manifests.".format(len(news), len(manifests)))

    attributes = {'menu': 'archive',
                  'news': news,
                  'manifests': manifests}

    return render(request, 'pages/archive.html', attributes)


def artist(request, artist_id):
    """Show artist information: about, art and contact."""

    # get the artist
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Sorry, but that artist does not exist!")
    logger.info("Showing details of " + artist.name + ".")

    # get his/her content...
    about_en_contents = Content.objects.filter(
        Q(section='AA'), Q(language='EN'), Q(identifier=artist.link)
    )
    about_nl_contents = Content.objects.filter(
        Q(section='AA'), Q(language='NL'), Q(identifier=artist.link)
    )
    contact_en_contents = Content.objects.filter(
        Q(section='CO'), Q(language='EN'), Q(identifier=artist.link)
    )
    contact_nl_contents = Content.objects.filter(
        Q(section='CO'), Q(language='NL'), Q(identifier=artist.link)
    )

    # ...and other entities
    works = Art.objects.filter(artist=artist)
    contact = Contact.objects.filter(artist=artist).get()
    logger.info('Contact: {}.'.format(contact))

    # get all labels in order...
    prices = LandPrice.objects.filter(active=True)
    all_art_labels = [p.header for p in prices if p.active]
    # ...and kick out the ones that are not used
    art_labels = []
    for label in all_art_labels:
        for work in works:
            if label == str(work.land_price.header):
                art_labels.append(label)
                break
    logger.info("Art labels: {}.".format(art_labels))

    attributes = {'menu': 'artist',
                  'about_en_contents': about_en_contents,
                  'about_nl_contents': about_nl_contents,
                  'contact_en_contents': contact_en_contents,
                  'contact_nl_contents': contact_nl_contents,
                  'works': works,
                  'art_labels': art_labels,
                  'contact': contact}

    return render(request, 'pages/artist.html', attributes)


def index(request):
    """The complete home page.

    Gets artists, news, manifests and land prices.
    """

    # get content...
    home_en_contents = Content.objects.filter(
        Q(section='HO'), Q(language='EN')
    )
    home_nl_contents = Content.objects.filter(
        Q(section='HO'), Q(language='NL')
    )

    # ...and all other entities
    artists = Artist.objects.filter(active=True)
    news = News.objects.filter(active=True).reverse()
    manifests = Manifest.objects.filter(active=True).reverse()
    prices = LandPrice.objects.filter(active=True)

    attributes = {'menu': 'home',
                  'home_en_contents': home_en_contents,
                  'home_nl_contents': home_nl_contents,
                  'artists': artists,
                  'news': news,
                  'manifests': manifests,
                  'prices': prices}

    return render(request, 'pages/index.html', attributes)
