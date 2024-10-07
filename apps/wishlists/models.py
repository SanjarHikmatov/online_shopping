from django.conf import settings
from django.db import models
from urllib3 import request

from apps.products.models import Product


class Wishlist(models.Model):
    class Meta:
        unique_together = (('user', 'product'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
