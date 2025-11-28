from os import name
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from user.models import User

class UserLoginform(AuthenticationForm) :

    class Meta:
        model = User
