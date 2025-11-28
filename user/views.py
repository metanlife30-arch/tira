from django.shortcuts import render
from django.contrib import auth
from user.forms import UserLoginform
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def login(request):
    
    if request.method=='POST':
        form = UserLoginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password'] 
            user = auth.authenticate(username=username, password=password)
            if user :
                auth.login(request,user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginform()
    conte = {"title":"Home - Авторизация",
             'form': form}
    return  render(request, "user/login.html",conte)

def registration(request):
    conte = {"title":"Home - Регистрация"}
    return  render(request, "user/registration.html",conte)

def profile(request):
    conte = {"title":"Home - Кабинет"}
    return  render(request, "user/profile.html",conte)

def logout(request):
    
    conte = {"title":"Home - Авторизация"}
    return  render(request, "user/about.html",conte)