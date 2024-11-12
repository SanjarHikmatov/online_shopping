
from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    payment_method = models.ForeignKey('general.PaymentMethod', on_delete=models.PROTECT)

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False, editable=False)
    paid_at = models.DateTimeField(blank=True, null=True)

    coupon = models.ForeignKey('coupons.Coupon', on_delete=models.PROTECT, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_paid and self.paid_at:
            self.paid_at = now()
        super().save(*args, **kwargs)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)