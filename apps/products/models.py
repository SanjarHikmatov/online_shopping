from django.db import models

from apps.categories.models import Category

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('JPY', 'JPY'),
    ("UZS", "UZS"),
)


class Product(models.Model):
    title = models.CharField(max_length=255)
    total_rating = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    currency = models.CharField(choices=CURRENCY_CHOICES, default='USD', max_length=5)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)