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
    
class EditSalonInfoForm(forms.Form):
    salon_name = forms.CharField(max_length=301)
    salon_openingtime = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    salon_closingtime = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    happyhour_times = forms.CharField(max_length=301)
    happyhour_days = forms.CharField(max_length=301)
    happyhour_discount = forms.DecimalField(max_digits=5, decimal_places=2)

    address_line1 = forms.CharField(max_length=255)
    address_line2 = forms.CharField(max_length=255)
    suburb = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=20)
    country = forms.CharField(max_length=20)

    # email = forms.EmailField()
    # phone_number = forms.CharField(max_length=20)

    # print(email)
    # print(phone_number)

    def save(self, user):
        salon_name = self.cleaned_data["salon_name"]
        salon_openingtime = self.cleaned_data["salon_openingtime"]
        salon_closingtime = self.cleaned_data["salon_closingtime"]
        happyhour_times = self.cleaned_data["happyhour_times"]
        happyhour_days = self.cleaned_data["happyhour_days"]
        happyhour_discount = self.cleaned_data["happyhour_discount"]

        addressline1 = self.cleaned_data["address_line1"]
        addressline2 = self.cleaned_data["address_line2"]
        suburb = self.cleaned_data["suburb"]
        state = self.cleaned_data["state"]
        postcode = self.cleaned_data["postcode"]
        country = self.cleaned_data["country"]

        
        current_user_id = user.id
        print(current_user_id)
        
        user_instance = get_object_or_404(User, id=current_user_id)
        salonowner_instance = get_object_or_404(SalonOwner, user=user_instance)
        saloninfo_instance = salonowner_instance.salon
        salon_address_instance = saloninfo_instance.salon_address

        print(f"user: {user_instance} salonowner: {salonowner_instance} saloninstance: {saloninfo_instance} boop")

        saloninfo_instance.salon_name = salon_name
        saloninfo_instance.salon_openingtime = salon_openingtime
        saloninfo_instance.salon_closingtime = salon_closingtime
        saloninfo_instance.happyhour_times = happyhour_times
        saloninfo_instance.happyhour_days = happyhour_days
        saloninfo_instance.happyhour_discount = happyhour_discount

        salon_address_instance.addressline1 = addressline1
        salon_address_instance.addressline2 = addressline2
        salon_address_instance.suburb = suburb
        salon_address_instance.state = state
        salon_address_instance.postcode = postcode
        salon_address_instance.country = country

        saloninfo_instance.save()
        salon_address_instance.save()

        print(f"user: {user_instance} salonowner: {salonowner_instance} saloninstance: {saloninfo_instance}, address: {salon_address_instance} boop2")
        return saloninfo_instance