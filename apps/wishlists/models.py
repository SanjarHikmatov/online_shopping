from django.conf import settings
from django.db import models



class Wishlist(models.Model):
    class Meta:
        unique_together = (('user', 'product'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
