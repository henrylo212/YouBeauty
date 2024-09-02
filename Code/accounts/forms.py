
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100)
    usable_password = None
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.can_authenticate_with_password = True
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user