from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Seller, SellerSocialLink


@admin.register(Seller)
class SellerAdmin(TranslationAdmin):
    pass


@admin.register(SellerSocialLink)
class SellerSocialLinkAdmin(TranslationAdmin):
    pass
