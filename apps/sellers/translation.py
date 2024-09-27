from modeltranslation.translator import TranslationOptions, register

from apps.sellers.models import Seller, SellerSocialLink


@register(Seller)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(SellerSocialLink)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('social_media', 'link')
