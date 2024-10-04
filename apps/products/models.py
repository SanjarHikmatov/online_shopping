from django.db import models
from apps.comments.models import ProductComment
from apps.ratings.models import ProductRating


class Product(models.Model):
    class Currency(models.TextChoices):
        USD = '0', ('USD')
        EUR = '1', ('EUR')
        JPY = '2', ('JPY')
        UZS = '3', ('UZS')

    title = models.CharField(max_length=255)
    avg_rating = models.DecimalField(max_digits=10, decimal_places=1, default=0, editable=False)
    comment_count = models.DecimalField(max_digits=10, decimal_places=1, default=0, editable=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    currency = models.CharField(choices=Currency.choices, default='USD', max_length=5)
    short_description = models.CharField(max_length=500)
    long_description = models.TextField()
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to='products/main/images%Y/%m/%d/', blank=True)

    def set_avg_rating(self):
        aggregate_amounts = ProductRating.objects.filter(
            product_id=self.pk).aggregate(
            avg=models.Avg('rating', default=0),
        )
        self.avg_rating = round(aggregate_amounts['avg'], 1)
        self.save()

    def set_comments_count(self):
        self.comment_count = ProductComment.objects.filter(product_id=self.pk).count()
        self.save()

    def __str__(self):
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/')
    ordering_number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.image
