from django.urls import path
from apps.products.views import product

urlpatterns = [
    path('products/', product, name='products')
    
]
