from django.shortcuts import render, get_object_or_404
from accounts.models import SalonInfo
from .forms import SalonForm
from .models import SalonOwner, SalonAddress, SalonInfo, SalonService
from django.contrib.auth.decorators import login_required


def SalonDetailView(request, salon_id):
    # extracts salon object according to the id and the services the salon offers
    salon = get_object_or_404(SalonInfo, pk=salon_id)
    services = SalonService.objects.filter(salon=salon)
    return render(request, 'salons/salon_page.html', { 'salon': salon, 'services': services, })

@login_required
def SalonRegistrationView(request):
    if request.method == 'POST':
        salon_form = SalonForm(request.POST, request.FILES)
        if salon_form.is_valid():

            # input data into SalonAddress table
            salon_address = SalonAddress.objects.create(
                address_line1=salon_form.cleaned_data['address_line1'],
                address_line2=salon_form.cleaned_data.get('address_line2', ''),
                state=salon_form.cleaned_data['state'],
                postcode=salon_form.cleaned_data['postcode'],
                country=salon_form.cleaned_data['country'],
            )

            # makes the table for SalonInfo
            salon_info = salon_form.save(commit=False)
            # adds the SalonAddress field
            salon_info.salon_address = salon_address
            salon_info.save()

            # links the salon to the salon owner
            salon_owner = request.user.salonowner
            salon_owner.salon = salon_info
            salon_owner.save()

            # redirects the salon owner to the salon dashboard
            return redirect('salon_dashboard')
    else:
        salon_form = SalonForm()

    return render(request, 'salons/salon_form.html', {'salon_form': salon_form})