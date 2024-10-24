from modeltranslation.translator import TranslationOptions, register
from apps.features.models import FeatureValue

@register(FeatureValue)
class FeatureValueTranslationOptions(TranslationOptions):
    fields = ('name',)
