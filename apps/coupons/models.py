from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
class Coupon(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    discount_percent = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )


class UsedCoupon(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)