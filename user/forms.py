from dataclasses import field
import email
from os import name
from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm, UserChangeForm
from user.models import User

class UserLoginform(AuthenticationForm) :
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ['username','password']

class UserRegistrationform(UserCreationForm) :
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

class ProfileForm(UserChangeForm) :
    image = forms.ImageField(required=False) # Необязательное поле
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['image','last_name','username','email','first_name']


