from django.urls import path

from apps.products.views import product_list

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
]