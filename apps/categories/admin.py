from django.contrib import admin

from apps.categories.models import Category

from apps.categories.filters import CategoryFilter
from modeltranslation.admin import TranslationAdmin



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_filter = (CategoryFilter,'id')
