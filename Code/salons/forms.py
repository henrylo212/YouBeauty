from django import forms
from .models import SalonInfo, SalonAddress, Service, SalonService


class SalonForm(forms.ModelForm):
    address_line1 = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255, required=False)
    state = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=10)
    country = forms.CharField(max_length=100)

    class Meta:
        model = SalonInfo
        fields = [
            'salon_name', 'salon_photo', 'salon_openingtime', 
            'salon_closingtime', 'happyhour_times', 
            'happyhour_days', 'happyhour_discount'
        ]
        
        
class SalonServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    duration = forms.DurationField(help_text="Enter duration in HH:MM:SS format")
    description = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = SalonService
        fields = ['service', 'price', 'duration', 'description']