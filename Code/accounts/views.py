from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def business_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.groups.filter(name='salon').exists():
                login(request, user)
                return redirect('profile')  
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'registration/business_login.html')

