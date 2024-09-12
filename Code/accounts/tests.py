from django.test import TestCase
from .models import UserType

class UserTypeTest(TestCase):
    def test_model_creation(self):
        """Test that a UserType object can be created successfully"""
        user_type = UserType.objects.create(type='admin')
        self.assertEqual(user_type.type, 'admin')
        self.assertIsNotNone(user_type.type_id)  # Check that type_id is auto-assigned
