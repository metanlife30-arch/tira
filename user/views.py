from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from traitlets import Instance
from user.forms import UserLoginform, UserRegistrationform, ProfileForm
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
                messages.success(request,f"{username} Вы успешно вошли в аккаунт")
                if request.POST.get('next',None):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
                
    else:
        form = UserLoginform()
    conte = {"title":"Home - Авторизация",
             'form': form}
    return  render(request, "user/login.html",conte)

def registration(request):
    if request.method=='POST':
    
        form = UserRegistrationform(data=request.POST)
        if form.is_valid():
            form.save()
            user=form.instance
            auth.login(request,user)
            messages.success(request,f"{user.username} Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationform()
    conte = {"title":"Home - Регистрация", "form":form }
    return  render(request, "user/registration.html",conte)
@login_required
def profile(request):
    if request.method=='POST':
        form = ProfileForm(data=request.POST, instance= request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Профиль успешно обновлён")
            return HttpResponseRedirect(reverse('user:profile'))
            
    else:
        form = ProfileForm(instance=request.user)

    conte = {"title":"Home - Кабинет", "form":form}
    return  render(request, "user/profile.html",conte)
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,f"{request.user.username} Вы вышли из аккаунта")
    conte = {"title":"Home - Авторизация"}
    return redirect(reverse('main:index'))

def user_basket(request):

    return  render(request, "user/user_basket.html")