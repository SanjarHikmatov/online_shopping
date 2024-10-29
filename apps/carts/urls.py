from django.urls import path

from apps.carts import views
app_name = 'carts'

urlpatterns = [
    path('cart_page/', views.cart_page, name='cart-page'),
    path('create_cart/<int:product_id>/', views.create_cart, name='create-cart' ),
    path('delete_cart/<int:product_id>/', views.delete_cart, name='delete-cart'),
    # path('create_quantity/<int:product_id>/', views.create_quantity, name='create-quantity'),
]