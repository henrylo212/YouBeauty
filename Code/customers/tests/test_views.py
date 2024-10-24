from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from salons.models import SalonInfo, SalonService, Service, SalonAddress
from customers.models import Customer, Booking
from datetime import time, timedelta, date

from unittest.mock import patch


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Log in the user to satisfy @login_required decorator
        self.client.login(username='testuser', password='testpass')

        # Create a customer associated with the user
        self.customer = Customer.objects.create(user=self.user, phone_number='0412345678')

        # Create sample SalonAddress
        address = SalonAddress.objects.create(
            address_line1="123 Main St",
            suburb="Sydney",
            state="NSW",
            postcode="2000",
            country="Australia"
        )

        # Create sample SalonInfo with required fields
        salon_info = SalonInfo.objects.create(
            salon_name="Test Salon",
            salon_address=address,
            salon_openingtime=time(9, 0),  # Added opening time
            salon_closingtime=time(17, 0),  # Added closing time
            happyhour_discount=20.0
        )

        # Create sample Service
        Service.objects.create(service_name="Haircut")

          # Create a Service and associate it with the salon
        service = Service.objects.create(service_name="Haircut")
        self.salon_service = SalonService.objects.create(
            salon=salon_info, service=service, price=50.0, 
            duration=timedelta(hours=1), description="A premium haircut."
        )

        self.booking = Booking.objects.create(
            customer=self.customer, salon_service=self.salon_service,
            date='2024-10-18', start_time='10:00', end_time='11:00'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')
        self.assertIn('salon_info', response.context)
    
    def test_make_bookings_view(self):
        # Pass the salon_service_id in the reverse function
        url = reverse('make_bookings', args=[self.salon_service.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_bookings.html')
    
    def test_top_salons_view(self):
        response = self.client.get(reverse('top_salons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salons/top_salons.html')
        self.assertIn('salons', response.context)
    
    def test_booking_confirmation_view(self):
        response = self.client.get(reverse('booking_confirmation', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_confirmation.html')
    
    def test_edit_booking(self):
        response = self.client.post(reverse('edit_booking', args=[self.booking.id]), {
            'date': '2024-10-19',
            'time': '12:00',
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.date, date(2024, 10, 19))
        self.assertEqual(self.booking.start_time, time(12, 0))  # Correct comparison

    def test_booking_cancellation(self):
        """Test that a booking can be cancelled successfully."""
        # Ensure the booking is not cancelled initially
        self.assertFalse(self.booking.is_cancelled, "The booking should not be cancelled initially.")

        # Cancel the booking by setting is_cancelled to True
        self.booking.is_cancelled = True
        self.booking.save()

        # Reload the booking from the database to verify the change
        cancelled_booking = Booking.objects.get(id=self.booking.id)
        self.assertTrue(cancelled_booking.is_cancelled, "The booking should be marked as cancelled.")

        # Ensure the __str__ method still works after cancellation
        booking_str = str(cancelled_booking)
        expected_str = f'Booking by testuser for Haircut'
        self.assertEqual(booking_str, expected_str, "__str__() method did not return the expected result after cancellation.")


class HappyHourViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        address = SalonAddress.objects.create(
            address_line1="123 Main St",
            suburb="Sydney",
            state="NSW",
            postcode="2000",
            country="Australia"
        )
        SalonInfo.objects.create(
            salon_name="Discount Salon",
            salon_address=address,
            happyhour_discount=15.0,
            salon_openingtime=time(9, 0),
            salon_closingtime=time(17, 0)
        )

    def test_happy_hour_view(self):
        response = self.client.get(reverse('happy_hour'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'happy_hour.html')
        self.assertIn('salons', response.context)

class MakeBookingsViewTest(TestCase):
    def setUp(self):
        # Set up client and create necessary data for the test
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        customer = Customer.objects.create(user=self.user, phone_number='0412345678')

        address = SalonAddress.objects.create(
            address_line1="123 Main St", suburb="Sydney", state="NSW", postcode="2000", country="Australia"
        )
        salon_info = SalonInfo.objects.create(
            salon_name="Test Salon", salon_address=address, 
            salon_openingtime=time(9, 0), salon_closingtime=time(17, 0), happyhour_discount=0.3,
            happyhour_times="4-7pm", happyhour_days="Mon-Wed"
        )
        service = Service.objects.create(service_name="Haircut")
        self.salon_service = SalonService.objects.create(
            salon=salon_info, service=service, price=50.0, 
            duration=timedelta(hours=1), description="A premium haircut."
        )

    def test_make_bookings_view(self):
        # Pass the salon_service_id in the reverse function
        url = reverse('make_bookings', args=[self.salon_service.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/make_bookings.html')
