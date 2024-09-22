from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from customers.models import Booking
from salons.models import SalonService
from salons.models import SalonInfo
from salons.models import Service
from salons.models import SalonAddress
import datetime

# from Code.accounts.models import Users

class CustomerTest(TestCase):
    def test_model_creation(self):
        """Test that a Customer object can be created successfully"""
        #Create a User object
        user = User.objects.create(username='test1', email="test1@email.com", password="123")

        #Create Customer
        customer = Customer.objects.create(user=user, phone_number='0412345678', profile_photo=None)
        self.assertEqual(customer.user, user)
        self.assertEqual(customer.phone_number, '0412345678')
        self.assertEqual(customer.profile_photo, None)

class BookingTest(TestCase):
    def test_model_creation(self):
        """Test that a Booking object can be created successfully"""
        #Create User (for the Customer) and Customer
        user = User.objects.create(username='test1', email="test1@email.com", password="123")
        customer = Customer.objects.create(user=user, phone_number='0412345678', profile_photo=None)

        #Create SalonAddress (for SalonInfo)
        salon_address = SalonAddress.objects.create(address_line1='Cleveland St', address_line2='Chippendale', state='NSW', postcode="2008", country="Australia")
        print(type(salon_address))
        #Create SalonInfo (for SalonService)
        # salon_info = SalonInfo.objects.create(salon_name="salon1", salon_address="23 Street St", salon_photo=None, 
        salon_info = SalonInfo.objects.create(salon_name="salon1", salon_address=salon_address, salon_photo=None, 
        salon_openingtime="09:00", salon_closingtime="16:00", happyhour_times="15:00", happyhour_days="Tuesday", happyhour_discount="0.4")
        
        #Create Service (for SalonService)
        service = Service.objects.create(service_name="Haircut")

        SalonAddress()

        #Create SalonService
        salon_service = SalonService.objects.create(salon=salon_info, service=service, price="50", duration=datetime.timedelta(hours=1), description="Quick haircut.")
        # salon = models.ForeignKey(SalonInfo, on_delete=models.CASCADE)
        # service = models.ForeignKey(Service, on_delete=models.CASCADE)
        # price = models.DecimalField(max_digits=10, decimal_places=2)
        # duration = models.DurationField()
        # description = models.TextField(blank=True, null=True)
        
        #Create Booking
        #set date, start time & end time
        date = "2024-04-23"
        start_time = "12:15"
        print(start_time)
        end_time = "1:15"

        booking = Booking.objects.create(customer=customer, salon_service=salon_service, date=date, start_time=start_time, end_time=end_time)
        self.assertEqual(booking.salon_service, salon_service)
        self.assertEqual(booking.date, date)
        self.assertEqual(booking.start_time, start_time)
        self.assertEqual(booking.end_time, end_time)
        self.assertEqual(booking.is_cancelled, False)
        # self.assertIsNotNone(user_type.type_id)  # Check that type_i