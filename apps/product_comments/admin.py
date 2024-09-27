
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.product_comments.models import ProductComment


@admin.register(ProductComment)
class ProductCommentAdmin(TranslationAdmin):
    list_display = ('message', 'name', 'email', 'product', 'user', 'created_at')