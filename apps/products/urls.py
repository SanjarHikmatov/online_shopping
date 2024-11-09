from django.urls import path

from apps.products import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('detail/<int:pk>/', views.product_detail, name='detail-page'),
    path('best-rating/', views.product_sort_by_avg_rating, name='show-avg-rating'),
    path('detail/feature/<int:pk>/', views.product_by_feature, name='product-by-feature'),
]
#     path('detail/feature/<int:pk>/', product_by_feature, name='product_by_feature'),
# ]