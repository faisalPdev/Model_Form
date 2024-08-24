from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name','username')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'placeholder': 'First Name','class': 'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'placeholder': 'Last Name','class': 'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'User Name','class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control'})


        

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email','class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    