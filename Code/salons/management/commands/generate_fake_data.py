from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta, time
from django.contrib.auth.models import User
from salons.models import SalonInfo, SalonAddress, SalonOwner, SalonService, Service
import random

# Use the Australian locale for Faker
fake = Faker('en_AU')

class Command(BaseCommand):
    help = 'Generate fake data for salons in Sydney with random happy hour times'

    def handle(self, *args, **kwargs):
        # Create some services
        services = ['Haircut', 'Nail Service', 'Facial', 'Massage', 'Hair Color']
        for service_name in services:
            Service.objects.get_or_create(service_name=service_name)

        # Function to generate a random happy hour time range
        def generate_happy_hour():
            start_hour = random.randint(9, 16)  # Generate a random start time between 9 AM and 4 PM
            end_hour = start_hour + random.randint(1, 2)  # Happy hour can last 1 to 2 hours
            start_time = time(start_hour, 0).strftime('%H:%M')
            end_time = time(end_hour, 0).strftime('%H:%M')
            return f'{start_time}-{end_time}'

        # Generate 5 salons with Sydney-based data
        for _ in range(5):
            # Create a fake Sydney address
            address = SalonAddress.objects.create(
                address_line1=fake.street_address(),
                address_line2=fake.secondary_address(),
                state='New South Wales',  # NSW state for Sydney
                postcode=fake.postcode(),  # Use AU-specific postcodes
                country='Australia'  # Set country to Australia
            )

            # Create a fake salon info with random happy hour times
            salon = SalonInfo.objects.create(
                salon_name=fake.company(),
                salon_address=address,
                salon_openingtime=fake.time(),
                salon_closingtime=fake.time(),
                happyhour_times=generate_happy_hour(),  # Generate random happy hour time
                happyhour_days=random.choice(['Mon-Fri', 'Mon-Sun', 'Sat-Sun']),  # Randomize happy hour days
                happyhour_discount=fake.pydecimal(left_digits=2, right_digits=2, positive=True)
            )

            # Create a fake salon owner with a Sydney-based phone number
            user = User.objects.create_user(
                username=fake.user_name(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )

            SalonOwner.objects.create(
                user=user,
                salon=salon,
                phone_number=fake.phone_number()  # Generates AU-based phone numbers
            )

            # Add some services to the salon
            for service in Service.objects.all():
                SalonService.objects.create(
                    salon=salon,
                    service=service,
                    price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
                    duration=timedelta(minutes=fake.random_int(min=30, max=120)),
                    description=fake.text()
                )

        self.stdout.write(self.style.SUCCESS('5 salons with Sydney addresses, phone numbers, and random happy hour times have been generated!'))