

from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from customers.models import Customer
from salons.models import SalonOwner
from .models import SalonInfo

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
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


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
    return render(request, 'profile/profile.html')

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

    return render(request, 'customers/login.html', {'form': form})

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
