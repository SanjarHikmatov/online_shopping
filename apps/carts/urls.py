from django.urls import path

from apps.carts.views import (

    delete_cart,
    set_cart_quantity,
    CartPageListView,
    CreateCartView,
)

app_name = 'carts'

urlpatterns = [
    path('cart_page/', CartPageListView.as_view(), name='cart-page'),
    path('create_cart/<int:product_id>/', CreateCartView.as_view(), name='create-cart' ),
    path('delete_cart/<int:product_id>/', delete_cart, name='delete-cart'),
    path('set/<int:cart_id>/',set_cart_quantity, name='set-cart-quantity'),
]