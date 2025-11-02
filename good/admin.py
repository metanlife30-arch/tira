from django.contrib import admin
from good.models import Category
from good.models import Products
# Register your models here.
#admin.site.register(Category)
#admin.site.register(Products)
# Register your models here.
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields: dict [str,tuple] = {"slug": ('name',)} 

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields: dict [str,tuple] = {"slug": ('name',)} 
