from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.products.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    model = Product
    list_display = ('title', 'price', 'avg_rating', 'category',)
    readonly_fields = ('old_price', 'price',)
    inlines = [ProductImageInline]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    model = ProductImage
    list_display = ('product', 'image')
