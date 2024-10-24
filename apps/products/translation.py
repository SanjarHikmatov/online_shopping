from modeltranslation.translator import TranslationOptions, register

from apps.products.models import Product

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)

