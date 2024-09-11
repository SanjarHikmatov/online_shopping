from django.db import models

from apps.products.models import Product


class Product_imege(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_imeges/image/%Y/%m/%d/')
    ordering_number = models.PositiveSmallIntegerField(default=0)
