from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductRating(models.Model):
    product = models.ForeignKey('products.Product', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
