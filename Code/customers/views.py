from django.shortcuts import render, redirect
from salons.models import SalonInfo
from .models import Booking, Customer
from salons.models import SalonService
from django.contrib.auth.decorators import login_required

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
    return render(request, 'homepage.html', {'salon_info': salon_info})
from salons.models import SalonInfo

def MakeBookingsView(request):
    return render(request, 'bookings/make_bookings.html')

@login_required
def make_bookings(request, salon_service_id):
    salon_service = SalonService.objects.get(id=salon_service_id)
    
    if request.method == 'POST':
        # Retrieve form data
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

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
        return redirect('booking_confirmation', booking_id=booking.id)
    
    return render(request, 'bookings/make_bookings.html', {'salon_service': salon_service})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})
