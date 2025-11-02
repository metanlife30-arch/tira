from django.urls import path
from good import views
app_name = 'good'
urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name= "catalog"),
     path('<slug:category_slug>/<int:page>/', views.catalog, name= "catalog"),
    path('product/<slug:product_slug>/', views.product, name= "product")

]