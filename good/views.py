from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse 
from good.models import Products
from good.models import Category
from django.core.paginator import Paginator
from good.utils import q_search
# Create your views here.
def catalog(request,category_slug=None):
    page = request.GET.get('page',1)
    on_sale = request.GET.get('on_sale',None)
    order_by = request.GET.get('order_by',None)
    query = request.GET.get('q',None)
    print(query)

    if category_slug == 'all':
        goods= Products.objects.all()
    elif query :
        goods =  q_search(query)
    
    else:
        goods= get_list_or_404(Products.objects.filter(category__slug= category_slug))
    if on_sale:
        goods= goods.filter(discount__gt=0)
    if order_by and order_by != 'default' :
        goods= goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    paginat= paginator.page(int(page))
    contet = {'goods':paginat ,
              'slug_url': category_slug}

    return  render(request, "good/catalog.html",contet)

def product(request,product_slug):
    product = Products.objects.get(slug= product_slug)
    conte = {"name":"О НАС",
             "product":product}
    return  render(request, "good/product.html",conte)