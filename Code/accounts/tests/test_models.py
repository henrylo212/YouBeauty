from django.test import TestCase
from ..models import UserType
from ..models import SalonAddress

class UserTypeTest(TestCase):
    def test_model_creation(self):
        """Test that a UserType object can be created successfully"""
        user_type = UserType.objects.create(type='admin')
        self.assertEqual(user_type.type, 'admin')
        self.assertIsNotNone(user_type.type_id)  # Check that type_id is auto-assigned

class SalonAddressTest(TestCase):
    def test_model_creation(self):
        """Test that a SalonAddress object can be created successfully"""
        salon_address = SalonAddress.objects.create(street='Cleveland St', suburb='Chippendale', state='NSW', postcode="2008")
        self.assertEqual(salon_address.street, 'Cleveland St')
        self.assertEqual(salon_address.suburb, 'Chippendale')
        self.assertEqual(salon_address.state, 'NSW')
        self.assertEqual(salon_address.postcode, '2008')
        self.assertIsNotNone(salon_address.address_id)  # Check that address_id is auto-assigned