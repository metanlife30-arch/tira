from dataclasses import field
from os import name
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user.models import User

class UserLoginform(AuthenticationForm) :
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ['username','password']
