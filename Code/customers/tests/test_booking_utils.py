from django.test import TestCase
from datetime import time, date, timedelta
from customers.models import Booking, Customer
from salons.models import SalonService, SalonInfo, Service, SalonAddress
from customers.booking_utils import is_time_slot_available  # Adjust import path if needed
from django.contrib.auth.models import User


class TimeSlotAvailabilityTestCase(TestCase):
    def setUp(self):
        # Create a salon address and info
        self.salon_address = SalonAddress.objects.create(
            address_line1="123 Main St",
            suburb="Sydney",
            state="NSW",
            postcode="2000",
            country="Australia"
        )
        self.salon_info = SalonInfo.objects.create(
            salon_name="Luxury Salon",
            salon_address=self.salon_address,
            salon_openingtime=time(9, 0),
            salon_closingtime=time(17, 0),
            happyhour_times="12:00-14:00",
            happyhour_days="Monday-Friday",
            happyhour_discount=10.00
        )

        # Create a service and associate it with the salon
        self.service = Service.objects.create(service_name="Haircut")
        self.salon_service = SalonService.objects.create(
            salon=self.salon_info,
            service=self.service,
            price=50.00,
            duration=timedelta(minutes=30),
            description="A premium haircut."
        )

        # Create a customer for bookings
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.customer = Customer.objects.create(user=self.user, phone_number="1234567890")

    def test_no_overlap(self):
        # No existing booking - time slot should be available
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertTrue(result, "The time slot should be available when no bookings overlap.")

    def test_exact_overlap(self):
        # Booking with the same start and end time
        Booking.objects.create(
            customer=self.customer,
            salon_service=self.salon_service,
            date=date.today(),
            start_time=time(10, 0),
            end_time=time(11, 0),
            is_cancelled=False
        )
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertFalse(result, "The time slot should not be available if it matches an existing booking.")

    def test_partial_overlap_start_before(self):
        # Booking that starts before and ends within the requested time slot
        Booking.objects.create(
            customer=self.customer,
            salon_service=self.salon_service,
            date=date.today(),
            start_time=time(9, 30),
            end_time=time(10, 30),
            is_cancelled=False
        )
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertFalse(result, "The time slot should not be available if another booking overlaps partially.")

    def test_partial_overlap_end_after(self):
        # Booking that starts within and ends after the requested time slot
        Booking.objects.create(
            customer=self.customer,
            salon_service=self.salon_service,
            date=date.today(),
            start_time=time(10, 30),
            end_time=time(11, 30),
            is_cancelled=False
        )
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertFalse(result, "The time slot should not be available if another booking overlaps partially.")

    def test_no_overlap_exact_end_match(self):
        # Booking that ends exactly when the requested time slot starts (no overlap)
        Booking.objects.create(
            customer=self.customer,
            salon_service=self.salon_service,
            date=date.today(),
            start_time=time(9, 0),
            end_time=time(10, 0),
            is_cancelled=False
        )
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertTrue(result, "The time slot should be available if another booking ends exactly at the start.")

    def test_cancelled_booking(self):
        # Cancelled booking should not block the time slot
        Booking.objects.create(
            customer=self.customer,
            salon_service=self.salon_service,
            date=date.today(),
            start_time=time(10, 0),
            end_time=time(11, 0),
            is_cancelled=True
        )
        result = is_time_slot_available(self.salon_service, date.today(), time(10, 0), time(11, 0))
        self.assertTrue(result, "The time slot should be available if the overlapping booking is cancelled.")
