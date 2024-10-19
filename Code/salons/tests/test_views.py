from django.test import TestCase, Client
from django.urls import reverse
from salons.models import SalonInfo, SalonService, SalonAddress, Service
from datetime import time, timedelta
# need to add more tests
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
        url = reverse('salon_details', args=[self.salon.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'salons/salon_page.html')
        self.assertIn('salon', response.context)
        self.assertIn('services', response.context)
