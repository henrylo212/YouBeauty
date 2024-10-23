from django.shortcuts import redirect
from django.urls import reverse

# this function ensures that a salon owner user cannot access any other pages until they complete salon registration
class SalonRegistrationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'salonowner'):
            salon_owner = request.user.salonowner
            
            # If the salon owner hasn't registered a salon yet, redirect them to the salon registration form
            if not salon_owner.salon and request.path != reverse('salons:salon_form'):
                return redirect(reverse('salons:salon_form'))

        response = self.get_response(request)
        return response


class RestrictCustomerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths customers should not access
        restricted_paths = [
            reverse('forBusiness'),
            reverse('business_profile_home'),
            reverse('business_profile_settings'),
            reverse('business_profile_calendar'),
            reverse('salon_register'),
            reverse('business_login'),
            reverse('salon_form'),
        ]

        if request.user.is_authenticated:
            # If the user is a customer
            if hasattr(request.user, 'customer'):
                for restricted_path in restricted_paths:
                    if request.path.startswith(restricted_path):
                        return redirect('home')  # Redirect customer to customer home page

        response = self.get_response(request)
        return response
    
    
class RestrictSalonOwnerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths salon owners should not access
        restricted_paths = [
            reverse('customer_register'),
            reverse('bookings'),
            reverse('profile'),
            reverse('login'),
            reverse('search_results'),
            reverse('happy_hour'),
            reverse('top_salons'),
            reverse('home'),
        ]
        
        if request.user.is_authenticated:
            # If the user is a salon owner
            if hasattr(request.user, 'salonowner'):
                for restricted_path in restricted_paths:
                    if request.path.startswith(restricted_path):
                        return redirect('business_profile_home')  # Redirect salon owner to business profile home

        response = self.get_response(request)
        return response