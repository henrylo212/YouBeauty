from django.test import TestCase
# from .models import 
from salons.models import SalonAddress

class SalonAddressTest(TestCase):
    def test_model_creation(self):
        """Test that a SalonAddress object can be created successfully"""
        salon_address = SalonAddress.objects.create(address_line1='Cleveland St', address_line2='Chippendale', state='NSW', postcode="2008", country="Australia")
        # salon_address = SalonAddress.objects.create(street='Cleveland St', suburb='Chippendale', state='NSW', postcode="2008")
        self.assertEqual(salon_address.address_line1, 'Cleveland St')
        self.assertEqual(salon_address.address_line2, 'Chippendale')
        self.assertEqual(salon_address.state, 'NSW')
        self.assertEqual(salon_address.postcode, '2008')
        self.assertEqual(salon_address.country, 'Australia')
        # self.assertIsNotNone(salon_address.address_id)  # Check that address_id is auto-assigned