from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm

from .models import SalonInfo

def RegistrationView(request):
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
    salon_info = SalonInfo.objects.all()  
    return render(request, 'homepage.html', {'salon_info': salon_info})

def FAQView(request):
    return render(request, 'faq.html')

def profileView(request):
    return render(request, 'profile/profile.html')


def bookingsView(request):
    return render(request, 'bookings.html')

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

