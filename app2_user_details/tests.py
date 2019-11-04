from django.test import TestCase
from .models import UserDetail

# Test UserDetails.

class UserDetailsTests(TestCase):
    
    """
    Here we'll define the tests that we'll run against our UserDetails model
    """
    
    def test_str(self):
        test_name=UserDetail(user_name='Kitty')
        self.assertEqual(str(test_name), 'Kitty')
