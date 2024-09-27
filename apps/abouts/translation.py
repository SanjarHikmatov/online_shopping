from modeltranslation.translator import TranslationOptions, register

from apps.abouts.models import About

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

