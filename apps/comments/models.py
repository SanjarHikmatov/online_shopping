from django.db import models
from django.conf import settings

class ProductComment(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
