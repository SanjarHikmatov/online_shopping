from modeltranslation.translator import TranslationOptions, register

from apps.abouts.models import About

@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

