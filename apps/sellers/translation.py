from modeltranslation.translator import TranslationOptions, register

from apps.sellers.models import Seller, SellerSocialLink


@register(Seller)
class SellerTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(SellerSocialLink)
class SellerSocialLinkTranslationOptions(TranslationOptions):
    fields = ('social_media', 'link')
