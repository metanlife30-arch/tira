from django.shortcuts import render
from django.http import HttpResponse 
from good.models import Category
# Create your views here.
def index(request):
    category = Category.objects.all()
    contex = {'contex':category }
    return  render(request, "main/index.html",context=contex)

def about(request):
    conte = {"name":"О НАС"}
    return  render(request, "main/about.html",conte)

