from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse 
from good.models import Products
from good.models import Category
from django.core.paginator import Paginator
# Create your views here.
def catalog(request,category_slug,page=1):
    if category_slug == 'all':
        goods= Products.objects.all()
    else:
        goods= get_list_or_404(Products.objects.filter(category__slug= category_slug))
    paginator = Paginator(goods, 3)
    paginat= paginator.page(page)
    contet = {'goods':paginat ,
              'slug_url': category_slug}

    return  render(request, "good/catalog.html",contet)

def product(request,product_slug):
    product = Products.objects.get(slug= product_slug)
    conte = {"name":"О НАС",
             "product":product}
    return  render(request, "good/product.html",conte)