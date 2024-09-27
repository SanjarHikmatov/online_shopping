from modeltranslation.translator import TranslationOptions, register

from apps.product_comments.models import ProductComment

@register(ProductComment)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'message')