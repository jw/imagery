from django.test import TestCase
from imagery.impart.models import LandPrice, Art


class ArtTestCase(TestCase):

    def setUp(self):
        LandPrice.objects.create(type='P', order=1)
        LandPrice.objects.create(type='D', order=2)

        # Art.objects.create()

    def test_landprice_type(self):
        """Show the landprice type"""
        painting = LandPrice.objects.get(type='P')
        drawing = LandPrice.objects.get(type='D')
        self.assertEqual(painting.get_type_display(), 'Painting')
        self.assertEqual(drawing.get_type_display(), 'Drawing')
