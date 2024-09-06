from django.shortcuts import render
from .models import SalonInfo

def salon_list(request):
    salons = SalonInfo.objects.all()  
    return