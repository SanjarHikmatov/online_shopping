from django.db import models



class ProductFeature(models.Model):
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    feature_value = models.ForeignKey(to='features.FeatureValue', on_delete=models.CASCADE, related_name='feature_value')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Enter the price of the UZS')
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2)

    class Meta:
        unique_together = (('product', 'feature_value'),)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.old_price, self.product.price = self.old_price, self.price
        self.product.save()

    def __str__(self):
        return str(self.feature_value)