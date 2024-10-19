from django.test import TestCase
from django.urls import reverse
# from ..views import UserType
from django.contrib.auth.models import User
# from salons.views import SalonAddress
# from accounts.views import RegistrationView

# class RegistrationViewTest(TestCase):
#     def test_get_RegistrationView(self):
#         client_response = self.client.get(reverse("register"))
#         self.assertEqual(client_response.status_code, 200)

class FAQViewTest(TestCase):
    def test_get_FAQView(self):
        client_response = self.client.get(reverse("faq"))
        self.assertEqual(client_response.status_code, 200)

class ProfileViewTest(TestCase):
    def test_get_ProfileView(self):
        client_response = self.client.get(reverse("profile"))
        self.assertEqual(client_response.status_code, 200)

class BookingsViewTest(TestCase):
    def test_get_BookingsView(self):
        client_response = self.client.get(reverse("bookings"))
        self.assertEqual(client_response.status_code, 200)

class ForBusinessViewTest(TestCase):
    def test_get_ForBusinessView(self):
        client_response = self.client.get(reverse("forBusiness"))
        self.assertEqual(client_response.status_code, 200)

# class CustomerLoginTest(TestCase):
#     def test_get_CustomerLogin(self):
#         client_response = self.client.get(reverse("customer_login"))
#         self.assertEqual(client_response.status_code, 200)

# class SalonLoginTest(TestCase):
#     def test_get_SalonLogin(self):
#         client_response = self.client.get(reverse("salon_login"))
#         self.assertEqual(client_response.status_code, 200)
