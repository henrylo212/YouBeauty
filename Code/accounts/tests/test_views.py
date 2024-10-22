from django.test import TestCase
from django.urls import reverse
# from ..views import UserType
from django.contrib.auth.models import User
from customers.models import Customer, Booking
from salons.models import SalonOwner, SalonAddress, SalonInfo, SalonService, Service
from datetime import datetime, timedelta
from datetime import time
# from accounts.views import RegistrationView


class CustomerLoginViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_get_CustomerLoginView(self):
        response = self.client.get(reverse('login'))  # Assuming 'login' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_post_CustomerLoginView_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        self.assertRedirects(response, '/customer/')  # Redirect after successful login

    def test_post_CustomerLoginView_fail(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Stays on login page if failed
        self.assertTemplateUsed(response, 'registration/login.html')


class BusinessLoginViewTest(TestCase):
    def setUp(self):
        # Create a test business user
        self.user = User.objects.create_user(username='businessuser', password='password')

    def test_get_BusinessLoginView(self):
        response = self.client.get(reverse('business_login'))  # Assuming 'business_login' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/business_login.html')

    def test_post_BusinessLoginView_success(self):
        response = self.client.post(reverse('business_login'), {'username': 'businessuser', 'password': 'password'})
        self.assertRedirects(response, '/accounts/forBusiness/')

    def test_post_BusinessLoginView_fail(self):
        response = self.client.post(reverse('business_login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/business_login.html')


class CustomerRegistrationViewTest(TestCase):
    def test_get_CustomerRegistrationView(self):
        response = self.client.get(reverse('customer_register'))  # Assuming 'customer_register' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/customer_register.html')

    def test_post_CustomerRegistrationView_success(self):
        response = self.client.post(reverse('customer_register'), {
            'username': 'newuser',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'phone_number': '1234567890',
            'email': 'newuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'profile_photo': ''
        })

        # Check that the user is redirected to the home page
        self.assertRedirects(response, reverse('home'))

        # Verify that the user was created in the database
        self.assertTrue(User.objects.filter(username='newuser').exists())
        user = User.objects.get(username='newuser')

        # Verify that the associated Customer was created
        self.assertTrue(Customer.objects.filter(user=user).exists())
        customer = Customer.objects.get(user=user)

        # Check that the customer's phone number was saved correctly
        self.assertEqual(customer.phone_number, '1234567890')

    def test_post_CustomerRegistrationView_fail(self):
        response = self.client.post(reverse('customer_register'), {
            'username': '',  # Invalid data
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'phone_number': '1234567890'
        })
        self.assertEqual(response.status_code, 200)  # Remain on the same page if failed
        self.assertTemplateUsed(response, 'registration/customer_register.html')


class SalonOwnerRegistrationViewTest(TestCase):
    def test_get_SalonOwnerRegistrationView(self):
        response = self.client.get(reverse('salon_register'))  # Assuming 'business_register' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/business_register.html')

    # def test_post_SalonOwnerRegistrationView_success(self):
    #     response = self.client.post(reverse('salon_register'), {
    #         'username': 'businessuser',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123',
    #         'phone_number': '0987654321',
    #         'email': 'businessuser@example.com',
    #         'first_name': 'Business',
    #         'last_name': 'User'
    #     })

    #     # Verify that the user is redirected to the salon form page after successful registration
    #     self.assertRedirects(response, reverse('salons:salon_form'))

    #     # Check that the user is created in the database
    #     self.assertTrue(User.objects.filter(username='businessuser').exists())
    #     user = User.objects.get(username='businessuser')

    #     # Check that the linked SalonOwner instance is created
    #     self.assertTrue(SalonOwner.objects.filter(user=user).exists())
    #     salon_owner = SalonOwner.objects.get(user=user)

    #     # Verify the phone number is correctly stored
    #     self.assertEqual(salon_owner.phone_number, '0987654321')

    # def test_post_SalonOwnerRegistrationView_existing_username(self):
    #     # Create an existing user to test against
    #     User.objects.create_user(username='differentuser', password='password')

    #     # Simulate a POST request using an existing username
    #     response = self.client.post(reverse('salon_register'), {
    #         'username': 'existinguser',
    #         'password1': 'strongpassword123',
    #         'password2': 'strongpassword123',
    #         'phone_number': '0987654321',
    #         'email': 'test@example.com',
    #         'first_name': 'Existing',
    #         'last_name': 'User'
    #     })

    #     # Check that the response status is 200 (form re-renders)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'registration/business_register.html')

    #     # Verify that the form displays an error for the username field
    #     self.assertContains(response, "This username is already taken.")

    # def test_post_SalonOwnerRegistrationView_password_mismatch(self):
    #     # Simulate a POST request with mismatched passwords
    #     response = self.client.post(reverse('salon_register'), {
    #         'username': 'newbusinessuser',
    #         'password1': 'strongpassword123',
    #         'password2': 'differentpassword',
    #         'phone_number': '0987654321',
    #         'email': 'test2@example.com',
    #         'first_name': 'New',
    #         'last_name': 'User'
    #     })

    #     # Check that the response status is 200 (form re-renders)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'registration/business_register.html')

    #     # Verify that no user is created
    #     self.assertFalse(User.objects.filter(username='newbusinessuser').exists())

    #     # Ensure form error about password mismatch is shown
    #     self.assertFormError(response, 'form', 'password2', "The two password fields didn’t match.")
    
    def test_post_SalonOwnerRegistrationView_fail(self):
        response = self.client.post(reverse('salon_register'), {
            'username': 'businessuser',
            'password1': 'strongpassword123',
            'password2': 'differentpassword',  # Passwords do not match
            'phone_number': '0987654321'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/business_register.html')

class BusinessProfileHomeViewTest(TestCase):
    def setUp(self):
        # Create a test salon owner and a salon
        self.user = User.objects.create_user(username='salonowner', password='password')
        self.salon_owner = SalonOwner.objects.create(user=self.user, phone_number='1234567890')
        self.client.login(username='salonowner', password='password')

    def test_get_BusinessProfileHomeView(self):
        response = self.client.get(reverse('business_profile_home'))  # Assuming 'business_profile_home' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile_home.html')


class BookingsViewTest(TestCase):
    def setUp(self):
        # Create a test user and a customer
        self.user = User.objects.create_user(username='customer', password='password')
        self.customer = Customer.objects.create(user=self.user, phone_number='1234567890')
        self.client.login(username='customer', password='password')

    def test_get_BookingsView(self):
        response = self.client.get(reverse('bookings'))  # Assuming 'bookings' is the URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/bookings.html')




class BusinessProfileSettingsViewTest(TestCase):
    def setUp(self):
        # Create test users
        self.customer_user = User.objects.create_user(username='customeruser', password='password')
        self.salon_owner_user = User.objects.create_user(username='salonowneruser', password='password')

        # Create Customer and SalonOwner linked to the test users
        self.customer = Customer.objects.create(user=self.customer_user, phone_number='1234567890')
        self.salon_address = SalonAddress.objects.create(
            address_line1="123 Main St", suburb="Testville", state="TS", postcode="12345", country="Testland"
        )
        self.salon_info = SalonInfo.objects.create(
            salon_name="Test Salon",
            salon_openingtime="09:00:00",
            salon_closingtime="18:00:00",
            happyhour_times="12:00-14:00",
            happyhour_days="Monday-Friday",
            happyhour_discount=20.00,
            salon_address=self.salon_address
        )
        self.salon_owner = SalonOwner.objects.create(
            user=self.salon_owner_user, phone_number='0987654321', salon=self.salon_info
        )

    def test_get_BusinessProfileSettingsView_as_customer(self):
        # Log in as a customer and make a GET request
        self.client.login(username='customeruser', password='password')
        response = self.client.get(reverse('business_profile_settings'))

        # Check the response status and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile_settings.html')

        # Verify context data to check user is identified as a customer
        self.assertTrue(response.context['is_customer'])
        self.assertFalse(response.context['is_salon_owner'])

    def test_get_BusinessProfileSettingsView_as_salon_owner(self):
        # Log in as a salon owner and make a GET request
        self.client.login(username='salonowneruser', password='password')
        response = self.client.get(reverse('business_profile_settings'))

        # Check the response status and template used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile_settings.html')

        # Verify context data to check user is identified as a salon owner
        self.assertTrue(response.context['is_salon_owner'])
        self.assertFalse(response.context['is_customer'])

    def test_post_BusinessProfileSettingsView_edit_salon_owner(self):
        # Log in as a salon owner and make a POST request to update details
        self.client.login(username='salonowneruser', password='password')
        response = self.client.post(reverse('business_profile_settings'), {
            'profile_name': 'Updated Name',
            'email': 'updated@example.com',
            'phone_number': '1112223333'
        })

        # Verify redirect after successful form submission
        self.assertRedirects(response, reverse('business_profile_settings'))

        # Check that the salon owner details were updated
        self.salon_owner.refresh_from_db()
        self.assertEqual(self.salon_owner.user.first_name, 'Updated')
        self.assertEqual(self.salon_owner.user.last_name, 'Name')
        self.assertEqual(self.salon_owner.user.email, 'updated@example.com')
        self.assertEqual(self.salon_owner.phone_number, '1112223333')

    # def test_post_BusinessProfileSettingsView_edit_salon_info(self):
    #     # Log in as a salon owner and make a POST request to update salon info
    #     self.client.login(username='salonowneruser', password='password')
    #     response = self.client.post(reverse('business_profile_settings'), {
    #         'salon_name': 'Updated Test Salon',
    #         'salon_openingtime': '10:00:00',
    #         'salon_closingtime': '19:00:00',
    #         'happyhour_times': '13:00-15:00',
    #         'happyhour_days': 'Tuesday-Friday',
    #         'happyhour_discount': '15.00',
    #         'address_line1': '456 New St',
    #         'address_line2': '',
    #         'suburb': 'Newville',
    #         'state': 'NS',
    #         'postcode': '67890',
    #         'country': 'Newland'
    #     })

    #     # Verify redirect after successful form submission
    #     self.assertRedirects(response, reverse('business_profile_settings'))

    #     # Check that the salon info was updated correctly
    #     self.salon_info.refresh_from_db()
    #     self.salon_address.refresh_from_db()
    #     self.assertEqual(self.salon_info.salon_name, 'Updated Test Salon')
    #     self.assertEqual(self.salon_info.salon_openingtime.strftime('%H:%M:%S'), '10:00:00')
    #     self.assertEqual(self.salon_info.happyhour_times, '13:00-15:00')
    #     self.assertEqual(self.salon_address.address_line1, '456 New St')

    def test_post_BusinessProfileSettingsView_invalid_form(self):
        # Log in as a salon owner and submit an invalid form (missing required field)
        self.client.login(username='salonowneruser', password='password')
        response = self.client.post(reverse('business_profile_settings'), {
            'salon_name': ''  # Invalid, missing required field
        })

        # Ensure the form re-renders and doesn't redirect
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile_settings.html')

        # Ensure no changes were saved
        self.salon_info.refresh_from_db()
        self.assertNotEqual(self.salon_info.salon_name, '')


class BusinessProfileCalendarViewTest(TestCase):
    def setUp(self):
        # Create a test user and associate it with a salon owner
        self.user = User.objects.create_user(username='salonowneruser', password='password')
        self.salon_address = SalonAddress.objects.create(
            address_line1="123 Test St", suburb="Testville", state="TS", postcode="12345", country="Testland"
        )
        self.salon_info = SalonInfo.objects.create(
            salon_name="Test Salon",
            salon_openingtime="09:00:00",
            salon_closingtime="18:00:00",
            happyhour_times="12:00-14:00",
            happyhour_days="Monday-Friday",
            happyhour_discount=20.00,
            salon_address=self.salon_address
        )
        self.salon_owner = SalonOwner.objects.create(
            user=self.user, phone_number='1234567890', salon=self.salon_info
        )

        # Create a test customer
        self.customer_user = User.objects.create_user(username='customeruser', password='password')
        self.customer = Customer.objects.create(user=self.customer_user, phone_number='1112223333')

        # Create a test service and salon service
        self.service = Service.objects.create(service_name="Haircut")
        self.salon_service = SalonService.objects.create(
            salon=self.salon_info,
            service=self.service,
            price=50.00,
            duration=timedelta(hours=1),
            description="Basic haircut service"
        )

        # Create test bookings for the salon, associated with the customer
        self.booking1 = Booking.objects.create(
            salon_service=self.salon_service,
            customer=self.customer,  # Add customer to fix IntegrityError
            date=datetime.now().date(),
            start_time=datetime.now().time(),
            end_time=(datetime.now() + timedelta(hours=1)).time()
        )
        self.booking2 = Booking.objects.create(
            salon_service=self.salon_service,
            customer=self.customer,  # Add customer to fix IntegrityError
            date=(datetime.now() + timedelta(days=1)).date(),
            start_time=(datetime.now() + timedelta(hours=2)).time(),
            end_time=(datetime.now() + timedelta(hours=3)).time()
        )

    def test_get_BusinessProfileCalendarView(self):
        # Log in as the salon owner
        self.client.login(username='salonowneruser', password='password')

        # Make a GET request to the calendar view
        response = self.client.get(reverse('business_profile_calendar'))  # Replace with actual URL name

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'business_profile_calendar.html')

        # Verify that the correct bookings are included in the context
        bookings = response.context['bookings']
        self.assertEqual(len(bookings), 2)

        # Verify the booking data for the first booking
        self.assertEqual(bookings[0]['id'], self.booking1.id)
        self.assertEqual(bookings[0]['date'], self.booking1.date.strftime('%Y-%m-%d'))
        self.assertEqual(bookings[0]['title'], self.booking1.salon_service.service.service_name)
        self.assertEqual(bookings[0]['start_time'], self.booking1.start_time.strftime('%H:%M'))
        self.assertEqual(bookings[0]['end_time'], self.booking1.end_time.strftime('%H:%M'))
        self.assertEqual(bookings[0]['color'], 'blue')

    def test_get_BusinessProfileCalendarView_no_bookings(self):
        # Log in as the salon owner and delete existing bookings
        self.client.login(username='salonowneruser', password='password')
        Booking.objects.all().delete()

        # Make a GET request to the calendar view
        response = self.client.get(reverse('business_profile_calendar'))  # Replace with actual URL name

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Verify that there are no bookings in the context
        bookings = response.context['bookings']
        self.assertEqual(len(bookings), 0)

# class SearchResultsViewTest(TestCase):
#     def setUp(self):
#         # Set up test data
#         self.address1 = SalonAddress.objects.create(
#             address_line1="123 Main St", suburb="Testville", state="TS", postcode="12345", country="Testland"
#         )
#         self.address2 = SalonAddress.objects.create(
#             address_line1="456 Another Rd", suburb="Anothertown", state="AT", postcode="67890", country="Testland"
#         )

#         self.salon1 = SalonInfo.objects.create(
#             salon_name="Best Salon",
#             salon_address=self.address1,
#             salon_openingtime=time(9, 0),
#             salon_closingtime=time(18, 0),
#             happyhour_times="12:00-14:00",
#             happyhour_days="Monday-Friday",
#             happyhour_discount=20.00
#         )
#         self.salon2 = SalonInfo.objects.create(
#             salon_name="Glam Salon",
#             salon_address=self.address2,
#             salon_openingtime=time(10, 0),
#             salon_closingtime=time(19, 0),
#             happyhour_times="14:00-16:00",
#             happyhour_days="Saturday-Sunday",
#             happyhour_discount=15.00
#         )

#         self.service1 = Service.objects.create(service_name="Haircut")
#         self.service2 = Service.objects.create(service_name="Manicure")

#         self.salon_service1 = SalonService.objects.create(
#             salon=self.salon1, service=self.service1, price=50.00, duration=30, description="Basic Haircut"
#         )
#         self.salon_service2 = SalonService.objects.create(
#             salon=self.salon2, service=self.service2, price=30.00, duration=20, description="Basic Manicure"
#         )

#     def test_get_search_results_empty(self):
#         response = self.client.get(reverse('search_results'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'search_results.html')
#         # Check that no search filters are applied
#         self.assertContains(response, "search-results")

#     def test_post_search_results_no_filters(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': '',
#             'location': '',
#             'service': ''
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'search_results.html')
#         # Expect to get all salon services
#         self.assertContains(response, "Best Salon")
#         self.assertContains(response, "Glam Salon")

#     def test_post_search_results_by_name(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': 'Best',
#             'location': '',
#             'service': ''
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Best Salon")
#         self.assertNotContains(response, "Glam Salon")

#     def test_post_search_results_by_location(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': '',
#             'location': 'Testville',
#             'service': ''
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Best Salon")
#         self.assertNotContains(response, "Glam Salon")

#     def test_post_search_results_by_service(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': '',
#             'location': '',
#             'service': 'manicure'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertNotContains(response, "Best Salon")
#         self.assertContains(response, "Glam Salon")

#     def test_post_search_results_multiple_filters(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': 'Glam',
#             'location': 'Anothertown',
#             'service': 'manicure'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertNotContains(response, "Best Salon")
#         self.assertContains(response, "Glam Salon")

#     def test_post_search_results_no_match(self):
#         response = self.client.post(reverse('search_results'), {
#             'searched': 'Unknown',
#             'location': 'Nowhere',
#             'service': 'Pedicure'
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No results found")

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
