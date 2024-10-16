from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.abouts.models import About


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    group_fieldsets = True
    #
    # def has_add_permission(self, request):
    #     """
    #     This function work for delete (+add User) in admin page after create one obj
    #     """
    #     if About.objects.exists():
    #         return False
    #     return True
