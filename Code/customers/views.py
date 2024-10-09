from django.shortcuts import render, redirect, get_object_or_404
from salons.models import SalonInfo
from .models import Booking, Customer
from customers.models import Customer
from salons.models import SalonService
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.core.mail import send_mail

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

        subject = f"Booking confirmed for {booking.customer.user.username} at {salon_service.salon.salon_name}"
        message = (
            f"Dear {booking.customer.user.username},\n\n"
            f"Thank you for booking with Youbeauty. Your {booking.salon_service} booking "
            f"on {date}, {start_time_str} at {salon_service.salon.salon_name} is confirmed.\n\n"
            f"Sincerely,\nYoubeauty"
        )
        recipient_list = [customer.user.email]
        send_mail(subject, message, 'your_email@example.com', recipient_list)


        return redirect('booking_confirmation', booking_id=booking.id)
    
    return render(request, 'bookings/make_bookings.html', {'salon_service': salon_service})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        if 'cancel_booking' in request.POST:
            booking.delete()
            return redirect('bookings')
        else:
            booking.date = request.POST['date']
            booking.start_time = request.POST['time']
            booking.save()
            return redirect('bookings')

    return render(request, 'bookings/edit_booking.html', {'booking': booking})