from django.urls import path

from apps.wishlists import views

app_name = "wishlists"
urlpatterns = [
    path('wishlist_create/', views.wishlist_create, name='wishlist-create'),
    path('', views.wishlist_page, name='wishlist-page'),
    path('delete_wishlist/<int:product_id>', views.wishlist_delete, name='wishlist-delete'),
]
