from django.db import models
from django.conf import settings


class ProductRating(models.Model):
    product = models.ForeignKey('products.Product', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
