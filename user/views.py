from django.shortcuts import render

# Create your views here.
def login(request):
    conte = {"title":"Home - Авторизация"}
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