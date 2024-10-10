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
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

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
    
    
class CustomerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    profile_photo = forms.ImageField(required=False)
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'profile_photo']

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


# class RegistrationForm(UserCreationForm):
#     ROLE_CHOICES = [
#         ('customer', 'Customer'),
#         ('salonowner', 'Salon Owner'),
#     ]
#     role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
#     phone_number = forms.CharField(max_length=20)
#     usable_password = None
    
#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         self.fields['username'].help_text = None
#         self.fields['password1'].help_text = None
#         self.fields['password2'].help_text = None

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'role', 'phone_number']



class EditProfileForm(forms.Form):
    profile_name = forms.CharField(max_length=301)
    # first_name = forms.CharField(max_length=150)
    # last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)

    # print(profile_name)
    print(email)
    print(phone_number)

    # class Meta:
    #     model = Customer
    #     fields = ['user.first_name', 'user.last_name', 'user.email', 'phone_number']

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
        # customer_instance = get_object_or_404(Customer, id=current_customer_id)
        
        # user_instance = get_object_or_404(User, id=current_user_id)

        print(f"user: {user_instance} customer: {customer_instance} boop")

        user_instance.first_name = first_name
        user_instance.last_name = last_name
        user_instance.email = email
        customer_instance.phone_number = phone_number

        user_instance.save()
        customer_instance.save()
    

        # user = User.objects.filter(id=customer.user.id).update(first_name=first_name, last_name=last_name, email=email)
        # print(user)
        # customer = Customer.objects.filter(user=customer.id).update(user=user, phone_number=phone_number)

        # User.objects.update(first_name=first_name, last_name=last_name, email=email)
        # Customer.objects.update(user=user,phone_number=phone_number)

        print(f"user: {user_instance} customer: {customer_instance} boop number 2")
        return user_instance, customer_instance


        

