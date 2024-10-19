from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customers.models import Customer
from salons.models import SalonOwner
from django.shortcuts import get_object_or_404
from django.test import TestCase
from accounts.forms import EditProfileForm
from django.contrib.auth.models import User
from customers.models import Customer
from django.test import TestCase
from accounts.forms import CustomerRegistrationForm
from django.contrib.auth.models import User

class CustomerRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'customer',
            'email': 'customer@example.com',
            'first_name': 'Test',
            'last_name': 'Customer',
            'password1': 'fsX£9!h4,{57',
            'password2': 'fsX£9!h4,{57',
            'phone_number': '9876543210',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_password_mismatch(self):
        form_data = {
            'username': 'customer',
            'email': 'customer@example.com',
            'first_name': 'Test',
            'last_name': 'Customer',
            'password1': 'fsX£9!h4,{57',
            'password2': 'fsX£9!h4,{5',  # Passwords don't match
            'phone_number': '9876543210',
        }
        form = CustomerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail due to password mismatch

        



class EditProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', first_name='Test', last_name='User', email='testuser@example.com'
        )
        self.customer = Customer.objects.create(user=self.user, phone_number='1234567890')

    def test_valid_form(self):
        form_data = {
            'profile_name': 'New Name',
            'email': 'newemail@example.com',
            'phone_number': '0987654321'
        }
        form = EditProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

        user, customer = form.save(self.user)
        self.assertEqual(user.first_name, 'New')
        self.assertEqual(user.last_name, 'Name')
        self.assertEqual(user.email, 'newemail@example.com')
        self.assertEqual(customer.phone_number, '0987654321')

    def test_invalid_email(self):
        form_data = {
            'profile_name': 'New Name',
            'email': 'invalid-email',  # Invalid email format
            'phone_number': '0987654321'
        }
        form = EditProfileForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail due to invalid email
        self.assertIn('email', form.errors)
