from itertools import product

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title', 'price', 'avg_rating', 'category',)