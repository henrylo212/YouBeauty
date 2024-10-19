from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from .forms import SalonForm, SalonServiceForm
from .models import SalonOwner, SalonAddress, SalonInfo, SalonService


def SalonDetailView(request, salon_id):
    '''
    Handles information about the salon detail page

    This view handlers information about the salon detail page

    Args:
        request (HttpRequest): The HTTP request object, which is GET

    Template:
        'salons/salon_page.html': The template used to display the salon detail page
    
    '''
    # extracts salon object according to the id and the services the salon offers
    salon = get_object_or_404(SalonInfo, pk=salon_id)
    services = SalonService.objects.filter(salon=salon)
    return render(request, 'salons/salon_page.html', { 'salon': salon, 'services': services, })


@login_required
def SalonRegistrationView(request):
    '''
    Handles information about the salon registration page

    This view handlers information about the salon registration page

    Args:
        request (HttpRequest): The HTTP request object, which can be GET or POST

    Template:
        'salons/salon_form.html': The template used to display the salon registration page
    
    '''
    # Create a factory so that the user can start with adding one service to their salon, and then add more if they want
    SalonServiceFormSet = formset_factory(SalonServiceForm, extra=1, can_delete=True)

    if request.method == 'POST':
        salon_form = SalonForm(request.POST, request.FILES)
        service_formset = SalonServiceFormSet(request.POST)

        if salon_form.is_valid() and service_formset.is_valid():

            # Create and save SalonAddress
            salon_address = SalonAddress.objects.create(
                address_line1=salon_form.cleaned_data['address_line1'],
                address_line2=salon_form.cleaned_data.get('address_line2', ''),
                suburb=salon_form.cleaned_data['suburb'],
                state=salon_form.cleaned_data['state'],
                postcode=salon_form.cleaned_data['postcode'],
                country=salon_form.cleaned_data['country'],
            )

            # Create and save SalonInfo with the associated SalonAddress
            salon_info = salon_form.save(commit=False)
            salon_info.salon_address = salon_address
            salon_info.save()

            # Associate the salon with the salon owner
            salon_owner = request.user.salonowner
            salon_owner.salon = salon_info
            salon_owner.save()

            # Save each service offered by the salon
            for service_form in service_formset:
                if service_form.cleaned_data:
                    SalonService.objects.create(
                        salon=salon_info,
                        service=service_form.cleaned_data['service'],
                        price=service_form.cleaned_data['price'],
                        duration=service_form.cleaned_data['duration'],
                        description=service_form.cleaned_data['description']
                    )

            # Redirect to the salon dashboard or home page
            # return redirect('salon_dashboard')
            return redirect('forBusiness')
    else:
        salon_form = SalonForm()
        service_formset = SalonServiceFormSet()

    return render(request, 'salons/salon_form.html', {'salon_form': salon_form, 'service_formset': service_formset})


def salon_list(request):
    '''
    Handles information about the list of salons

    This view handlers information about the list of salons

    Args:
        request (HttpRequest): The HTTP request object, which is GET
    
    '''
    salons = SalonInfo.objects.all()  
    return salons

def salon_details(request, salon_id):
    '''
    Handles information about the salon details

    This view handlers information about the salon details

    Args:
        request (HttpRequest): The HTTP request object, which is GET
        salon_id (): The id of the salon whose details will be fetched

    Template:
        'salons/salon_page.html': The template used to display the salon details
    
    '''
    salon = get_object_or_404(SalonInfo, pk=salon_id)
    return render(request, 'salons/salon_page.html', {'salon': salon})

def salon_dashboard(request):
    # Assuming the logged-in user is a SalonOwner
    salon_owner = SalonOwner.objects.get(user=request.user)
    salon = salon_owner.salon
    bookings = Booking.objects.filter(salon_service__salon=salon, is_cancelled=False).order_by('date', 'start_time')
    return render(request, 'salon_dashboard.html', {'bookings': bookings})