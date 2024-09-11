from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField, EmailField

from apps.products.models import Product


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = CharField(max_length=120)
    email = EmailField(max_length=120)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
