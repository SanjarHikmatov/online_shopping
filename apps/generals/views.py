from django.shortcuts import redirect
from django.conf import settings
from django.utils.translation import activate, get_language



def set_language(request, lang):
    if lang not in settings.MODELTRANSLATION_LANGUAGE:
        lang = settings.LANGUAGE_CODE
    activate(lang)
    return redirect(request.META['HTTP_REFERER'])
