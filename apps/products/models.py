from decimal import Decimal

from django.db import models
from apps.comments.models import ProductComment
from apps.general.models import General
from apps.product_features.models import ProductFeature
# from apps.ratings.models import ProductRating




class Product(models.Model):


    title = models.CharField(max_length=255)
    avg_rating = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal('0'),
        editable=False
    )
    comment_count = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=Decimal('0'),
        editable=False
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Enter the price of the UZS',
        editable=False
    )
    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        help_text='Enter the old price of the UZS'

    )
    currency = models.CharField(
        choices=General.CurrencyChoices.choices,
        default='UZS',
        max_length=5
    )
    short_description = models.CharField(max_length=500)
    long_description = models.TextField(max_length=500)
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    added_at = models.DateTimeField(auto_now_add=True)

    main_image = models.ImageField(upload_to='products/images/%Y/%m/%d/', blank=True)
    @property
    def get_features(self):
        product_features = ProductFeature.objects.prefetch_related('feature_value').filter(product_id=self.pk)
        features = {}
        for product_feature in product_features:
            for value in product_feature.feature_value.all():
                if value.feature_id not in features:
                    features[value.feature_id] = {
                        'id': value.feature_id,
                        'name': value.feature.name,
                        'value': [
                            {'id': value.pk, 'name': value.name}
                        ]
                    }
                else:
                    features[value.feature_id]['values'].append(
                        {'id': value.pk, 'name': value.name}
                    )
        return list(features.values())

    def set_avg_rating(self):
            aggregate_amounts = ProductComment.objects.filter(
                product_id=self.pk
            ).aggregate(
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
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/')
    ordering_number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):

        return self.image


