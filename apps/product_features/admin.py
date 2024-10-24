from django.contrib import admin

from apps.product_features.models import ProductFeature


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('product', 'feature_value', 'price', 'old_price' )
    min_num = 1
