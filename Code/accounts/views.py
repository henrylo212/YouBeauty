from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
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
