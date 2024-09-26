

from .forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from customers.models import Customer
from salons.models import SalonOwner
# from .models import SalonInfo
from salons.views import SalonRegistrationView
from django.urls import reverse
# from .models import Users

# Think of all these views as just webpages. Views (in the form of html/css pages) of the database almost

def RegistrationView(request):
    """
    Handle user registration.

    This view handles user registration by processing a form submission.
    If the request method is POST and the form is valid, the new user is created,
    authenticated, and logged in automatically. Upon successful registration,
    the user is redirected to the home page. If the request method is GET, the 
    registration form is displayed.

    Args:
        request (HttpRequest): The HTTP request object, which may be GET or POST.

    Returns:
        HttpResponse: 
            - If the request method is POST and the form is valid, redirects to the home page.
            - If the request method is GET or the form is invalid, renders the registration form page.
        
    Context:
        form (RegistrationForm): The registration form, either blank or filled with submitted data.

    Template:
        'registration/register.html': The template used to display the registration form.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # extract data from form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            
            # authenticate the user
            user = authenticate(username=username, password=password)
            login(request, user)
            
            if role == 'salonowner':
                # salon owner is redirected to salon registration page
                return redirect(reverse('salons:salon_form')) 
            else:
                # customer is redirected to homepage
                return redirect('home') 
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


# def extractSalonInfoView(request):
#     '''
#     Handles information about the salon homepage

#     This view handlers information about the salon homepage.

#     Args:
#         request (HttpRequest): The HTTP request object, which is GET

#     Template:
#         'homepage.html': The template used to display the salon homepage
    
#     '''
#     salon_info = SalonInfo.objects.all()  
#     return render(request, 'homepage.html', {'salon_info': salon_info})

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

def profileView(request):
    '''
    Handles information about the user profile 

    This view handles information about the user profile

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'profile/profile.html': The template used to display the user profile information
    
    '''
    # def getCurrentUser(request):
    # current_user_id = request.user
    # current_user = Users.objects.get(pk=current_user_id)
    # # return render(request, 'profile.html', {'user_info': user_info})
    # return render(request, 'profile.html', {'current_user_info': current_user})

    # user_profiles = Users.objects.all() 
    # for user in user_profiles:
    #     print(f"UID: {user.user_id}")
    #     print(f"Username: {user.username}")
    #     print("\n")
    # print(user_profiles)
    # user = get_object_or_404(Users, pk=request.user.id)
    # user = get_object_or_404(Users, username = "capstone")
    
    # user = get_object_or_404(Users, pk=request.user.id)
    # user = get_object_or_404(Users, pk=2)
    # print(user.user_id)
    # print(request.user)
    # print(request.user.username)
    current_username = request.user.username #get username of logged in user
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
        profile_photo = customer.profile_photo
        print(profile_photo)
        return render(request, 'profile/profile.html' , 
        {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
        'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo})
    elif is_salon_owner:
        user = salon_owner.user
        phone_number = salon_owner.phone_number
        salon = salon_owner.salon
        return render(request, 'profile/profile.html' , 
        {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
        'user': user, 'phone_number': phone_number, 'salon': salon})
    else:
        user = current_user
        phone_number = ""
        profile_photo = None
        print(profile_photo)
        return render(request, 'profile/profile.html' , 
        {'is_customer': is_customer, 'is_salon_owner': is_salon_owner, 
        'user': user, 'phone_number': phone_number, 'profile_photo': profile_photo})

    # customer = get_object_or_404(Customer, username=current_username) #get Customer w/ current username
    # salon_owner = get_object_or_404(SalonOwner, username=current_username) #get SalonOwner w/ current username

    # user = get_object_or_404(Users, username = current_username)
    #todo: line above is creating issues - not linked to authorization users, only accounts.
    # print(user)
    # return render(request, 'profile/profile.html', {"user_profiles": user_profiles})

    # if request.method == 'POST':
    #     edit_form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect('home')  
    # else:
    #     form = RegistrationForm()


    return render(request, 'profile/profile.html') #, {'current_username': current_username})

def editProfileView(request):
    return render(request, 'profile/edit_profile.html')

def bookingsView(request):
    return render(request, 'bookings/bookings.html')

def forBusinessView(request):
    return render(request, 'forBusiness.html')


def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                
                if hasattr(user, 'customer'):
                    login(request, user)
                    return redirect('customer_dashboard')
                else:
                    form.add_error(None, "This account is not registered as a customer.")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def salon_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                
                if hasattr(user, 'salonowner'):
                    login(request, user)
                    return redirect('salon_dashboard')
                else:
                    form.add_error(None, "This account is not registered as a salon owner.")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'salons/login.html', {'form': form})



