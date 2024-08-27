from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import login, authenticate
from .forms import RegistrationForm

# def test(request):
#     return HttpResponse("Hello world!")

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