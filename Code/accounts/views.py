

from .forms import SalonOwnerRegistrationForm, CustomerRegistrationForm, EditProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from customers.models import Customer, Booking
from salons.models import SalonOwner
from salons.models import SalonInfo
# from .models import SalonInfo
from salons.views import SalonRegistrationView
from django.urls import reverse
# from .models import Users
import datetime
from django.contrib.auth.views import LoginView

class CustomerLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        # Redirect to the default dashboard for regular users
        return "/customer/"

class BusinessLoginView(LoginView):
    template_name = "registration/business_login.html"

    def get_success_url(self):
        # Redirect to the business dashboard after a successful login
        return "/accounts/forBusiness/"



# Think of all these views as just webpages. Views (in the form of html/css pages) of the database almost


def CustomerRegistrationView(request):
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


def SalonRegistrationView(request):
    if request.method == 'POST':
        form = SalonOwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            
            # creates SalonOwner object linked to this user
            SalonOwner.objects.create(user=user, phone_number=phone_number)

            #authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            # redirect to the salon registration form
            return redirect(reverse('salons:salon_form')) 
    else:
        form = SalonOwnerRegistrationForm()
    return render(request, 'registration/business_register.html', {'form': form})


def BusinessProfileHomeView(request):

    return render(request, 'business_profile_home.html')

def BusinessProfileSettingsView(request):

    return render(request, 'business_profile_settings.html')

def BusinessProfileCalendarView(request):

    return render(request, 'business_profile_calendar.html')

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
    Handles information about the user profile 

    This view handles information about the user profile

    Args:
        request (HttpRequest): The HTTP request object, which is GET

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
            # return redirect("success")

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


# def editProfileView(request):
#     return render(request, 'profile/edit_profile.html')

def bookingsView(request):
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
    return render(request, 'forBusiness.html')


# def customer_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
                
#                 if hasattr(user, 'customer'):
#                     login(request, user)
#                     return redirect('customer_dashboard')
#                 else:
#                     form.add_error(None, "This account is not registered as a customer.")
#             else:
#                 form.add_error(None, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()

#     return render(request, 'registration/login.html', {'form': form})

# def salon_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
                
#                 if hasattr(user, 'salonowner'):
#                     login(request, user)
#                     return redirect('salon_dashboard')
#                 else:
#                     form.add_error(None, "This account is not registered as a salon owner.")
#             else:
#                 form.add_error(None, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()

#     return render(request, 'registration/business_login.html', {'form': form})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        location = request.POST.get('location', False)
        service = request.POST.get('service', False)
        salon_names = SalonInfo.objects.filter(salon_name__contains=searched)
        return render(request, 'search_results.html', {'searched':searched, 'salon_names':salon_names, 'location':location, 'service':service})
    else:
        return render(request, 'search_results.html')
    