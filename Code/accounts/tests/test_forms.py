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

         # Save with commit=False and ensure it's not in DB yet
        unsaved_user = form.save(commit=False)
        self.assertIsNone(unsaved_user.id)  # Unsaved user should have no ID yet

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
    
    def test_last_name_absent(self):
            # Provide only the first name in the 'profile_name'
            form_data = {
                'profile_name': 'OnlyFirst',  # No space for last name
                'email': 'newemail@example.com',
                'phone_number': '0987654321'
            }
            form = EditProfileForm(data=form_data)

            # Ensure the form is valid
            self.assertTrue(form.is_valid())

            # Save the form and verify the user and customer instances are updated correctly
            user, customer = form.save(self.user)

            self.assertEqual(user.first_name, 'OnlyFirst')  # First name should match input
            self.assertEqual(user.last_name, '-')  # Last name should be set to '-'
            self.assertEqual(user.email, 'newemail@example.com')  # Email should be updated
            self.assertEqual(customer.phone_number, '0987654321')  # Phone number should be updated


from accounts.forms import SalonOwnerRegistrationForm


class SalonOwnerRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'salonowner',
            'email': 'owner@example.com',
            'first_name': 'Salon',
            'last_name': 'Owner',
            'password1': 'fsX£9!h4,{57',
            'password2': 'fsX£9!h4,{57',
            'phone_number': '1234567890'
        }
        form = SalonOwnerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

         # Save with commit=False and ensure it doesn’t hit the DB immediately
        unsaved_user = form.save(commit=False)
        self.assertIsNone(unsaved_user.id)  # User shouldn't have an ID yet (unsaved)

    def test_missing_required_field(self):
        form_data = {
            'username': 'salonowner',
            'email': 'owner@example.com',
            'password1': 'fsX£9!h4,{57',
            'password2': 'fsX£9!h4,{57',
        }
        form = SalonOwnerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())  # Should fail because first_name and last_name are required
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
