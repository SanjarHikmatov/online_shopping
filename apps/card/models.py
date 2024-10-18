# from decimal import Decimal
#
# from django.db import models
#
#
#
# class ProductCard(models.Model):
#     product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
#     user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.product.name
