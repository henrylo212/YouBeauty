from django.db.models import Q
from customers.models import Booking

def is_time_slot_available(salon_service, date, start_time, end_time):
    overlapping_bookings = Booking.objects.filter(
        salon_service=salon_service,
        date=date,
        is_cancelled=False
    ).filter(
        Q(start_time__lt=end_time) & Q(end_time__gt=start_time)
    )
    print("Overlapping bookings count:", overlapping_bookings.count())  # Debugging

    return not overlapping_bookings.exists()
