from django.urls import path
from apps.coupons.views import check_coupon

app_name = 'coupon'
urlpatterns = [
    path('check/', check_coupon, name='check-coupon')
]
