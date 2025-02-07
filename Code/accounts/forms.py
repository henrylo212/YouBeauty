from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customers.models import Customer
from salons.models import SalonOwner
from django.shortcuts import get_object_or_404

class SalonOwnerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    usable_password = None
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(SalonOwnerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # makes first name and last name mandatory
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
    
    
class CustomerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    profile_photo = forms.ImageField(required=False)
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number', 'profile_photo']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # makes first name and last name mandatory
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class EditProfileForm(forms.Form):
    profile_name = forms.CharField(max_length=301)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    print(email)
    print(phone_number)


    def save(self, user):
        print(f"useeerrrr {user}")
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
        customer_instance = get_object_or_404(Customer, user=user_instance)
        print(f"user: {user_instance} customer: {customer_instance} boop")

        user_instance.first_name = first_name
        user_instance.last_name = last_name
        user_instance.email = email
        customer_instance.phone_number = phone_number

        user_instance.save()
        customer_instance.save()
        print(f"user: {user_instance} customer: {customer_instance} boop number 2")
        return user_instance, customer_instance


        