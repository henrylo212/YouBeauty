

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Sum, Avg, Count
from django.db.models import F, ExpressionWrapper, DurationField
from django.db.models.functions import Cast
from datetime import timedelta

from .forms import SalonOwnerRegistrationForm, CustomerRegistrationForm, EditProfileForm

from salons.forms import EditSalonOwnerForm, EditSalonInfoForm
from salons.views import SalonRegistrationView
from salons.models import SalonOwner, SalonInfo, SalonService, Service, SalonAddress

from customers.models import Customer, Booking


from django.urls import reverse

import datetime
from django.contrib.auth.views import LoginView

class CustomerLoginView(LoginView):
    '''
    Handles information about the customer login page

    This view handles information about the customer login page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'registration/login.html': The template used to display the customer login page
    
    '''
    template_name = "registration/login.html"

    def get_success_url(self):
        # Redirect to the default dashboard for regular users
        return "/customer/"

class BusinessLoginView(LoginView):
    '''
    Handles information about the salon login page

    This view handles information about the salon login page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'registration/business_login.html': The template used to display the salon login page
    
    '''
    template_name = "registration/business_login.html"

    def get_success_url(self):
        # Redirect to the business dashboard after a successful login
        return "/accounts/forBusiness/"



# Think of all these views as just webpages. Views (in the form of html/css pages) of the database almost


def CustomerRegistrationView(request):
    '''
    Handles information about the customer registration page

    This view handles information about the customer registration page.

    Args:
        request (HttpRequest): The HTTP request object, which can be GET or POST

    Template:
        'registration/customer_register.html': The template used to display the customer registration page
    
    '''
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, request.FILES)  # also requests user to upload profile photo
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            profile_photo = form.cleaned_data.get('profile_photo')

            # creates Customer object linked to this user
            Customer.objects.create(user=user, phone_number=phone_number, profile_photo=profile_photo)

            # authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            # redirect to the home page
            return redirect('home')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'registration/customer_register.html', {'form': form})


def SalonOwnerRegistrationView(request):
    '''
    Handles information about the salon registration page

    This view handles information about the salon registration page.

    Args:
        request (HttpRequest): The HTTP request object, which can be GET or POST

    Template:
        'registration/business_register.html': The template used to display the salon registration page
    
    '''
    if request.method == 'POST':
        form = SalonOwnerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                form.add_error('username', ValidationError('This username is already taken.'))
            else:
                user = form.save()
                phone_number = form.cleaned_data.get('phone_number')
                
                # creates SalonOwner object linked to this user
                SalonOwner.objects.create(user=user, phone_number=phone_number)

                # authenticate and log in the user
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)

                # redirect to the salon registration form
                return redirect(reverse('salons:salon_form'))
    else:
        form = SalonOwnerRegistrationForm()
    return render(request, 'registration/business_register.html', {'form': form})


def BusinessProfileHomeView(request):
    '''
    Handles information about the business profile home page

    This view handles information about the business profile home page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'business_profile_home.html': The template used to display the business profile home page
    
    '''

    is_salonowner = False
    current_user = request.user
    try:
        salon_owner = get_object_or_404(SalonOwner, user=current_user)
        salon = salon_owner.salon

        if salon is None or salon.salon_address is None:
            return redirect('salons:salon_form')  

        upcoming_bookings = Booking.objects.filter(salon_service__salon=salon, date__gte=timezone.now().date())
        print("Bookings: ", upcoming_bookings)

        today = timezone.now().date()
        completed_bookings = Booking.objects.filter(
            salon_service__salon=salon,
            date__lt=today,  # Filter bookings before today
            is_cancelled=False  # Exclude cancelled bookings, if needed
        )

        print(f"Completed bookings {completed_bookings}")

        total_revenue = completed_bookings.aggregate(total=Sum('salon_service__price'))['total']
        total_revenue = total_revenue or 0
        
        print(f"Total revenue: {total_revenue}")

        # Total number of bookings before today
        total_bookings_before_today = completed_bookings.count()
        print(f'Total Bookings Before Today: {total_bookings_before_today}')

        # Average price of services for bookings before today
        average_price_before_today = completed_bookings.aggregate(average_price=Avg('salon_service__price'))['average_price']
        average_price_before_today = average_price_before_today or 0
        print(f'Average Service Price Before Today: ${average_price_before_today:.2f}')


        total_canceled_bookings = Booking.objects.filter(
            date__lt=today,
            is_cancelled=True
        ).count()
        print(f'Total Canceled Bookings (all time): {total_canceled_bookings}')

        # Calculate total duration of bookings before today (in seconds)
        total_duration_before_today = completed_bookings.annotate(duration=ExpressionWrapper(F('end_time') - F('start_time'), output_field=DurationField())
                                                                  ).aggregate(total_duration=Sum('duration'))['total_duration']

        # If there are no bookings, default to 0
        total_duration_before_today = total_duration_before_today or timedelta(seconds=0)
        total_duration_in_minutes = total_duration_before_today.total_seconds()//60
        print(f"total duration before today: {total_duration_before_today.total_seconds()//60}")

        # Convert to hours and minutes if necessary
        total_hours = total_duration_before_today.total_seconds() // 3600
        total_minutes = (total_duration_before_today.total_seconds() % 3600) // 60

        # total_hour_int = int(total_hours)

        print(f'Total Duration Before Today: {int(total_hours)} hours and {int(total_minutes)} minutes')



        # Get the most booked service before today
        most_popular_service = completed_bookings.values('salon_service__service__service_name').annotate(service_count=Count('salon_service__service__service_name')).order_by('-service_count').first()

        # Extract service name and count
        if most_popular_service:
            service_name = most_popular_service['salon_service__service__service_name']
            service_count = most_popular_service['service_count']
            print(f'Most Popular Service Before Today: Service ID {service_name} with {service_count} bookings')
        else:
            service_name = ""
            service_count = 0
            print("No bookings found before today.")

        # revenue_per_hour = (float(total_revenue)/total_duration_in_minutes)*60
        if total_duration_in_minutes > 0:
            revenue_per_hour = (float(total_revenue) / total_duration_in_minutes) * 60
        else:
            revenue_per_hour = 0  # Set to 0 or handle this scenario differently

        return render(request, 'business_profile_home.html', {'is_salonowner': is_salonowner, 'upcoming_bookings': upcoming_bookings, 'completed_bookings':completed_bookings, 'total_revenue':total_revenue,
                                                              'total_bookings_before_today':total_bookings_before_today, 'avg_revenue_per_hour':revenue_per_hour, 'cancelled_bookings': total_canceled_bookings, 'avg_price_bookings':average_price_before_today, 
                                                              'service_name':service_name, 'service_count':service_count})
    except SalonOwner.DoesNotExist:
        return render(request, 'business_profile_home.html', {'is_salonowner': False})


def BusinessProfileSettingsView(request):
    '''
    Handles information about the business profile settings page

    This view handles information about the business profile settings page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'business_profile_settings.html': The template used to display the business profile settings page
    
    '''

    is_customer = False
    is_salon_owner = False
    user = request.user
    phone_number = ""
    profile_photo = None
    form = None
    saloninfo_form = None
    # if hasattr(user, 'salonowner'):
    # if not hasattr(user, 'customer'):
    #     #is not customer
    #     redirect()

    if request.method == 'POST':
        print("made it to POST")
        form = EditSalonOwnerForm(data=request.POST)
        saloninfo_form = EditSalonInfoForm(data=request.POST)

        # print(form.errors)
        print(saloninfo_form.errors)

        if form.is_valid():
            current_user = request.user
            print("in salon owner form")
            print(f"exists {SalonOwner.objects.filter(user=current_user).exists()}, {SalonOwner.objects.filter(user=current_user)}")

            form.save(user)

            messages.success(request, 'Profile changes have been successfully saved!')
            return redirect("business_profile_settings")
        
        if saloninfo_form.is_valid():
            # Saving salon info here
            print("are we in here?")
            current_user = request.user
            saloninfo_form.save(user)

            messages.success(request, 'Salon Info changes have been successfully saved!')
            return redirect("business_profile_settings")
    else:
        form = EditSalonOwnerForm()
        saloninfo_form = EditSalonInfoForm()


    if request.method == "GET":
        # current_username = request.user.username #get username of logged in user
        current_user = request.user #get logged in user
        print(current_user)
        is_customer = False
        is_salon_owner = False


        try:
            #try to get a customer
            customer = get_object_or_404(Customer, user=current_user) #get Customer w/ current username
            is_customer = True    
            # is_salon_owner = False
        except:
            try:
                #try to get a salon_owner
                salon_owner = get_object_or_404(SalonOwner, user=current_user) #get SalonOwner w/ current username
                is_salon_owner = True
                # is_customer = False 
            except:
                #is logged in but not a customer, and not a salon owner
                print("Not a customer. Not a salon owner.")

        if is_customer:
            user = customer.user
            phone_number = customer.phone_number
            try:
                if customer.profile_photo.url:
                    profile_photo = customer.profile_photo
            except:
                print("No profile photo file.")
                # profile_photo = None
            print(profile_photo)
            
            # Get upcoming bookings
            #date_gte= means: date is GREATER THAN OR EQUAL to 
            bookings = Booking.objects.filter(date__gte=datetime.date.today()).filter(customer=customer)
            print(bookings)

            return render(request, 'business_profile_settings.html' , 
            {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
            'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo,
            'bookings': bookings, 'form': form, 'saloninfo_form': saloninfo_form})
            # return render(request, 'registration/login.html', {'form': form})
        elif is_salon_owner:
            user = salon_owner.user
            phone_number = salon_owner.phone_number
            salon = salon_owner.salon
            salon_address = salon.salon_address

            # bookings = Booking.objects.filter(date__gte=datetime.date.today()).filter(customer=customer)
            # print(bookings)

            # Get all bookings for the salon by joining SalonInfo and Booking models
            # bookings = Booking.objects.filter(salon_service__salon=salon)
            # print("BOOKINGS: ", bookings)

            # salon_services = SalonService.objects.filter()


            return render(request, 'business_profile_settings.html' , 
            {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
            'user': user, 'phone_number': phone_number, 'salon': salon, 'form': form, 'saloninfo_form': saloninfo_form, 'salon_address': salon_address})
    else:
        user = request.user

    
    return render(request, 'business_profile_settings.html' , 
        {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
        'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo,
        'form': form, 'saloninfo_form': saloninfo_form})   

    
    # return render(request, 'business_profile_settings.html')


def BusinessProfileCalendarView(request):
    '''
    Handles information about the business profile calendar page
    '''

    user = request.user

    salon_owner = get_object_or_404(SalonOwner, user=user)

    salon = salon_owner.salon

    bookings = Booking.objects.filter(salon_service__salon=salon)

    booking_data = [
        {
            'id': booking.id,
            'date': booking.date.strftime('%Y-%m-%d'),
            'title': booking.salon_service.service.service_name,
            'start_time': booking.start_time.strftime('%H:%M'),
            'end_time': booking.end_time.strftime('%H:%M'),
            'color': 'blue'  
        }
        for booking in bookings
    ]

    
    context = {
        'bookings': booking_data
    }

    return render(request, 'business_profile_calendar.html', context)


def business_edit_booking(request, booking_id):
    # Fetch the booking using the booking_id
    booking = get_object_or_404(Booking, id=booking_id)

    # Fetch all services available for the salon that the booking is associated with
    services = SalonService.objects.filter(salon=booking.salon_service.salon)

    if request.method == 'POST':
        if 'cancel_booking' in request.POST:
            # Cancel the booking
            booking.delete()
            return redirect(reverse('business_profile_calendar'))
        else:
            # Update the booking details
            booking.date = request.POST.get('date')
            booking.start_time = request.POST.get('start_time')
            booking.end_time = request.POST.get('end_time')
            service_id = request.POST.get('service')
            booking.salon_service = get_object_or_404(SalonService, id=service_id)
            booking.save()
            return redirect('business_profile_calendar')

    # Pass the booking and available services to the template
    context = {
        'booking': booking,
        'services': services,
    }
    return render(request, 'business_edit_booking.html', context)

def FAQView(request):
    '''
    Handles information about the FAQ homepage

    This view handles information about the FAQ page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'faq.html': The template used to display the FAQ homepage
    
    '''
    return render(request, 'faq.html')

def AboutView(request):
    '''
    Handles information for the About page

    This view handles information for the About page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'about.html': The template used to display the About page
    
    '''
    return render(request, 'about.html')

def profileView(request):
    '''
    Handles information about the customer profile 

    This view handles information about the customer profile

    Args:
        request (HttpRequest): The HTTP request object, which can be GET or POST

    Template:
        'profile/profile.html': The template used to display the user profile information
    
    '''

    is_customer = False
    is_salon_owner = False
    user = request.user
    phone_number = ""
    profile_photo = None
    form = None
    # if hasattr(user, 'salonowner'):
    # if not hasattr(user, 'customer'):
    #     #is not customer
    #     redirect()

    if request.method == 'POST':
        print("made it to POST")
        form = EditProfileForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            current_user = request.user
            print(f"exists {Customer.objects.filter(user=current_user).exists()}, {Customer.objects.filter(user=request.user)}")
            customer = get_object_or_404(Customer, user=current_user) #get Customer w/ current user
            saved = form.save(user)  
            # user = form.save(user)
            print(user)
            # extract data from form
            profile_name = form.cleaned_data.get('profile_name')
            print(profile_name)
            # password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            print(email)
            phone_number = form.cleaned_data.get('phone_number')
            messages.success(request, 'Profile changes have been successfully saved!')
        

            return redirect("profile")
    else:
        form = EditProfileForm()


    if request.method == "GET":
        # current_username = request.user.username #get username of logged in user
        current_user = request.user #get logged in user
        print(current_user)
        is_customer = False
        is_salon_owner = False
        try:
            #try to get a customer
            customer = get_object_or_404(Customer, user=current_user) #get Customer w/ current username
            is_customer = True    
            # is_salon_owner = False
        except:
            try:
                #try to get a salon_owner
                salon_owner = get_object_or_404(SalonOwner, user=current_user) #get SalonOwner w/ current username
                is_salon_owner = True
                # is_customer = False 
            except:
                #is logged in but not a customer, and not a salon owner
                print("Not a customer. Not a salon owner.")

        if is_customer:
            user = customer.user
            phone_number = customer.phone_number
            try:
                if customer.profile_photo.url:
                    profile_photo = customer.profile_photo
            except:
                print("No profile photo file.")
                # profile_photo = None
            print(profile_photo)
            
            # Get upcoming bookings
            #date_gte= means: date is GREATER THAN OR EQUAL to 
            bookings = Booking.objects.filter(date__gte=datetime.date.today()).filter(customer=customer)
            print(bookings)

            return render(request, 'profile/profile.html' , 
            {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
            'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo,
            'bookings': bookings, 'form': form})
            # return render(request, 'registration/login.html', {'form': form})
        elif is_salon_owner:
            user = salon_owner.user
            phone_number = salon_owner.phone_number
            salon = salon_owner.salon
            return render(request, 'profile/profile.html' , 
            {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
            'user': user, 'phone_number': phone_number, 'salon': salon, 'form': form})
    else:
        user = request.user

    
    return render(request, 'profile/profile.html' , 
        {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
        'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo,
        'form': form})   


def bookingsView(request):
    '''
    Handles information about the bookings page

    This view handles information about the bookings page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'bookings/bookings.html': The template used to display the bookings page
    
    '''
    current_user = request.user
    is_customer = False
    try:
        #try to get a customer
        customer = get_object_or_404(Customer, user=current_user) #get Customer w/ current username
        is_customer = True    
        # is_salon_owner = False
    except:
        is_customer = False
    
    if is_customer:
        bookings = Booking.objects.filter(customer=customer)
        print(bookings)
        return render(request, 'bookings/bookings.html', {'bookings': bookings})
    else:
        return render(request, 'bookings/bookings.html', {'bookings': None})

    
def forBusinessView(request):
    '''
    Handles information about the for business page

    This view handles information about the for business page.

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'forBusiness.html': The template used to display the for business page
    
    '''
    return render(request, 'forBusiness.html')


def search_results(request):
    '''
    Handles information about the search results page

    This view handles information about the search results page.

    Args:
        request (HttpRequest): The HTTP request object, which can be GET or POST

    Template:
        'search_results.html': The template used to display the search results page
    
    '''
    salon_info = SalonInfo.objects.all()  
    services = Service.objects.all() 
    addresses = SalonAddress.objects.all() 
    if request.method == 'POST':
        searched = request.POST.get('searched', False).lower()
        location = request.POST.get('location', False).lower()
        service = request.POST.get('service', False).lower()
        salons_obj = []
        for obj_salon_service in SalonService.objects.all():
            salon_name = obj_salon_service.salon.salon_name.lower()
            service_name = obj_salon_service.service.service_name.lower()
            address = obj_salon_service.salon.salon_address.suburb.lower()
            if searched == '' and location == '' and service == '':
                salons_obj.append(obj_salon_service)
            elif location == '' and service == '':
                if searched in salon_name:
                    salons_obj.append(obj_salon_service)
            elif searched == '' and service == '':
                if location in address:
                    salons_obj.append(obj_salon_service)
            elif searched == '' and location == '':
                if service in service_name:
                    salons_obj.append(obj_salon_service)
            elif searched == '':
                if location in address:
                    if service in service_name:
                        salons_obj.append(obj_salon_service)
            elif location == '':
                if searched in salon_name:
                    if service in service_name:
                        salons_obj.append(obj_salon_service)
            elif service == '':
                if searched in salon_name:
                    if location in address:
                        salons_obj.append(obj_salon_service)
            else:
                if searched in salon_name:
                    if location in address:
                        if service in service_name:
                            salons_obj.append(obj_salon_service)
        return render(request, 'search_results.html', {'searched':searched, 'location':location, 'service':service, 'salons_obj':salons_obj, 
                                                       'salon_info': salon_info, 'services': services, 'addresses': addresses})
    else:
        return render(request, 'search_results.html', {'salon_info': salon_info, 'services': services, 'addresses': addresses})
    