from django import forms
from .models import SalonInfo, SalonAddress


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