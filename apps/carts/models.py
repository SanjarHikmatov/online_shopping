from django.conf import settings
from django.db import models



class ProductCard(models.Model):
    class Meta:
        unique_together = (('user', 'product'),)
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def sub_total(self):
        return self.product.price * self.quantity


