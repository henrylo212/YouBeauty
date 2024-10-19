from django import forms
from .models import SalonInfo, SalonAddress, Service, SalonService
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customers.models import Customer
from salons.models import SalonOwner
from django.shortcuts import get_object_or_404

class SalonForm(forms.ModelForm):
    address_line1 = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255, required=False)
    suburb = forms.CharField(max_length=100)
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

class EditSalonOwnerForm(forms.Form):
    profile_name = forms.CharField(max_length=301)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    print(email)
    print(phone_number)

    def save(self, user):
        profile_name = self.cleaned_data["profile_name"]
        email = self.cleaned_data["email"]
        phone_number = self.cleaned_data["phone_number"]

        first_last_name = profile_name.split(" ", 1)
        print(first_last_name)
        first_name = first_last_name[0]

        if len(first_last_name) < 2:
            last_name = "-"
        else:
            last_name = first_last_name[1]
        
        current_user_id = user.id
        print(current_user_id)
        
        user_instance = get_object_or_404(User, id=current_user_id)
        salonowner_instance = get_object_or_404(SalonOwner, user=user_instance)
        
        print(f"user: {user_instance} salonowner: {salonowner_instance} boop")

        user_instance.first_name = first_name
        user_instance.last_name = last_name
        user_instance.email = email
        salonowner_instance.phone_number = phone_number

        # Updating both the user and salonowner
        user_instance.save()
        salonowner_instance.save()

        print(f"user: {user_instance} salonowner: {salonowner_instance} boop number 2")
        return user_instance, salonowner_instance