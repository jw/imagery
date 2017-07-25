from django.test import TestCase
from imagery.impart.models import LandPrice, Artist, Art


class ArtTestCase(TestCase):

    def setUp(self):
        painting_type = LandPrice.objects.create(type='P', order=1)
        drawing_type = LandPrice.objects.create(type='D', order=2)
        artist = Artist.objects.create(name='artist')
        Art.objects.create(name='painting', artist=artist, x=10, y=20, land_price=painting_type)
        Art.objects.create(name='drawing', artist=artist, x=30, y=40, land_price=drawing_type)

    def test_landprice_type_display(self):
        """Show the landprice type"""
        painting = LandPrice.objects.get(type='P')
        drawing = LandPrice.objects.get(type='D')
        self.assertEqual(painting.get_type_display(), 'Painting')
        self.assertEqual(drawing.get_type_display(), 'Drawing')

    def test_art_price(self):
        """Calculate the art price"""
        painting = Art.objects.get(name='painting')
        drawing = Art.objects.get(name='drawing')
        self.assertEqual(painting.get_price(), 22.0)
        self.assertEqual(drawing.get_price(), 175)
