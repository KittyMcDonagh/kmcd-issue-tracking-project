from django.test import TestCase

# Import Feature model

from .models import Feature

# Test Feature.

class FeatureTests(TestCase):
    
    """
    Define the tests that will be run against the Feature model
    """
    
    def test_str(self):
        test_name=Feature(user_id='kitty')
        self.assertEqual(str(test_name), 'kitty')