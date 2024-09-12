from django.shortcuts import render, get_object_or_404
from accounts.models import SalonInfo

def salon_list(request):
    salons = SalonInfo.objects.all()  
    return

def salon_details(request, salon_id):
    salon = get_object_or_404(SalonInfo, pk=salon_id)
    return render(request, 'salons/salon_page.html', {'salon': salon})