from django.contrib import admin

from apps.features.models import Feature, FeatureValue
from apps.products.models import Product


class FeatureValueInline(admin.TabularInline):
    model = FeatureValue

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    model = Product
    inlines = [FeatureValueInline]

#
# @admin.register(FeatureValue)
# class FeatureValueAdmin(admin.ModelAdmin):
#     pass
