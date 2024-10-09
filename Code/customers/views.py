from django.shortcuts import render, redirect
from salons.models import SalonInfo
from .models import Booking, Customer
from customers.models import Customer
from salons.models import SalonService
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

def extractSalonInfoView(request):
    '''
    Handles information about the salon homepage

    This view handlers information about the salon homepage.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'homepage.html': The template used to display the salon homepage
    
    '''
    salon_info = SalonInfo.objects.all()  
    print(salon_info)
    return render(request, 'homepage.html', {'salon_info': salon_info})
from salons.models import SalonInfo

def MakeBookingsView(request):
    return render(request, 'bookings/make_bookings.html')

@login_required
def make_bookings(request, salon_service_id):
    salon_service = SalonService.objects.get(id=salon_service_id)
    print('Helooo?')
    if request.method == 'POST':
        print('Confirm booking button clicked!')
        try:
            # Check if a Customer object exists for the current user
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            # Handle the case where the customer doesn't exist
            print("Customer does not exist for this user. Redirecting to the registration page.")
            # You could redirect the user to a page where they can create a customer profile
            # return redirect('create_customer_profile')

        # Retrieve form data
        date = request.POST.get('date')
        start_time_str = request.POST.get('start_time')

        # Parse the start time and service duration
        start_time = datetime.strptime(start_time_str, '%H:%M').time()
        service_duration = salon_service.duration  # Assuming duration is a timedelta

        # Calculate the end time
        start_datetime = datetime.combine(datetime.now().date(), start_time)
        end_datetime = start_datetime + service_duration
        end_time = end_datetime.time()


        # Create a new booking
        customer = Customer.objects.get(user=request.user)
        booking = Booking.objects.create(
            customer=customer,
            salon_service=salon_service,
            date=date,
            start_time=start_time,
            end_time=end_time,
            is_cancelled=False
        )
        print(f"Booking created for {Customer.user} on {date} at {start_time}")

        return redirect('booking_confirmation', booking_id=booking.id)
    
    return render(request, 'bookings/make_bookings.html', {'salon_service': salon_service})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})
