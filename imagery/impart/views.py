from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from imagery.impart.models import News, LandPrice, Manifest, Artist, Art, Content, Contact

import collections
import logging
logger = logging.getLogger("imagery")


Language = collections.namedtuple('Language', 'code logo name')


def archive(request, page=1):
    """Show news and manifest archives."""

    news = News.objects.filter(archived=fintTrue)
    manifests = Manifest.objects.filter(archived=True)

    logger.error("Retrieved {} archived news entries, and {} archived manifests.".format(len(news), len(manifests)))

    attributes = {'menu': 'archive',
                  'news': news,
                  'manifests': manifests}

    return render(request, 'pages/archive.html', attributes)


def get_languages(request):
    """Get all the languages."""
    return [Language('NL', 'en.svg', 'English'),
            Language('EN', 'nl.svg', 'Nederlands')]


def get_language(request):
    """Get the selected language.

    English is the default."""
    code = request.GET.get('language', 'EN')
    if code == 'NL':
        return 'NL', 'EN'
    else:
        return 'EN', 'NL'


def artist(request, artist_id):
    """Show artist information: about, art and contact."""

    # get the artist
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404("Sorry, but that artist does not exist!")
    logger.info("Showing details of " + artist.name + ".")

    # get his/her content based on the selected language...

    about_contents_raw = Content.objects.filter(
        Q(section='AA'), Q(identifier=artist.link)
    )
    about_contents = {}
    for content in about_contents_raw:
        content_list = about_contents.setdefault(content.language, [])
        content_list.append(content)

    contact_contents_raw = Content.objects.filter(
        Q(section='CO'), Q(identifier=artist.link)
    )
    contact_contents = {}
    for content in contact_contents_raw:
        content_list = contact_contents.setdefault(content.language, [])
        content_list.append(content)

    (current_language, other_language) = get_language(request)
    languages = get_languages(request)

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
                  'artist': artist,
                  'current_language': current_language,
                  'other_language': other_language,
                  'languages': languages,
                  'about_contents': about_contents,
                  'contact_contents': contact_contents,
                  'works': works,
                  'art_labels': art_labels,
                  'contact': contact}

    return render(request, 'pages/artist.html', attributes)


def index(request):
    """The complete home page.

    Gets content, artists, news and manifests.
    """

    # get content...
    home_en_contents = Content.objects.filter(
        Q(section='HO'), Q(language='EN')
    )
    home_nl_contents = Content.objects.filter(
        Q(section='HO'), Q(language='NL')
    )

    (current_language, other_language) = get_language(request)
    languages = get_languages(request)

    landprice_contents_raw = Content.objects.filter(
        Q(section='LP')
    )

    landprice_contents = {}
    for content in landprice_contents_raw:
        content_list = landprice_contents.setdefault(content.language, [])
        content_list.append(content)

    logger.info(landprice_contents)

    # ...and all other entities
    artists = Artist.objects.filter(active=True)
    news = News.objects.filter(active=True).reverse()
    manifests = Manifest.objects.filter(active=True).reverse()

    attributes = {'menu': 'home',
                  'current_language': current_language,
                  'other_language': other_language,
                  'languages': languages,
                  'home_en_contents': home_en_contents,
                  'home_nl_contents': home_nl_contents,
                  'artists': artists,
                  'news': news,
                  'manifests': manifests,
                  'landprice_contents': landprice_contents}

    return render(request, 'pages/index.html', attributes)
