from django.test import TestCase, Client
from django.urls import reverse
from salons.models import SalonInfo, SalonService, SalonAddress, Service, SalonOwner
from datetime import time, timedelta
from salons.views import SalonDetailView
from salons.urls import *
from django.contrib.auth.models import User
from salons.forms import SalonForm, SalonServiceForm


class SalonDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Create address, salon, and service
        address = SalonAddress.objects.create(
            address_line1="123 Main St", suburb="Sydney", state="NSW", 
            postcode="2000", country="Australia"
        )
        self.salon = SalonInfo.objects.create(
            salon_name="Luxury Salon", salon_address=address,
            salon_openingtime=time(9, 0), salon_closingtime=time(17, 0),
            happyhour_times="14:00-16:00", happyhour_days="Weekdays",
            happyhour_discount=20.00
        )
        service = Service.objects.create(service_name="Haircut")
        
        # Use timedelta for duration
        SalonService.objects.create(
            salon=self.salon, service=service, price=50.0, duration=timedelta(hours=1)
        )

    def test_salon_detail_view(self):
        url = reverse('salon_page', args=[self.salon.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salons/salon_page.html')

        self.assertIn('salon', response.context)
        self.assertIn('services', response.context)

        self.assertEqual(response.context['salon'], self.salon)


class SalonRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='owner', password='testpass')
        self.client.login(username='owner', password='testpass')
        self.salon_owner = SalonOwner.objects.create(user=self.user)

    # def test_salon_registration_view_get(self):
    #     url = reverse('salon_form')
    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, 200)

    #     self.assertTemplateUsed(response, 'salons/salon_form.html')

    # def test_salon_registration_view_post_valid(self):
    #     url = reverse('salon_form')
    #     data = {
    #         'salon_name': 'Luxury Salon',
    #         'address_line1': '123 Main St',
    #         'suburb': 'Sydney',
    #         'state': 'NSW',
    #         'postcode': '2000',
    #         'country': 'Australia',
    #         'salon_openingtime': '09:00',
    #         'salon_closingtime': '17:00',
    #     }
    #     response = self.client.post(url, data)

    #     self.assertEqual(response.status_code, 200)  # Redirects on success

    #     # print(SalonInfo.objects)
    #     # self.assertTrue(SalonInfo.objects.filter(salon_name='Luxury Salon').exists())

    # def test_salon_registration_view_post_invalid(self):
    #     url = reverse('salon_form')
    #     data = {'salon_name': ''}  # Missing required fields
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 200)  # Stays on the same page
    # #     self.assertFormError(response, 'salon_form', 'salon_name', 'This field is required.')

# class SalonListViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         # Create salons
#         address = SalonAddress.objects.create(
#             address_line1="123 Main St", suburb="Sydney", state="NSW", 
#             postcode="2000", country="Australia"
#         )
#         SalonInfo.objects.create(
#             salon_name="Luxury Salon", salon_address=address, 
#             salon_openingtime=time(9, 0), salon_closingtime=time(17, 0), happyhour_times="14:00-16:00", happyhour_days="Weekdays",
#             happyhour_discount=20.00
#         )

#     def test_salon_list_view(self):
#         url = reverse('salon_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('salons', response.context)
#         self.assertEqual(len(response.context['salons']), 1)  # We created one salon