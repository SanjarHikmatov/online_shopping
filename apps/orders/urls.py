from django.urls import path

from apps.orders import views
urlpatterns = [
    path('', views.checkout, name='checkout-page'),
    path('create_order', views.create_order, name='create-order'),

]
