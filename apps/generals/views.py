from django.shortcuts import redirect
from django.conf import settings
from django.utils.translation import activate



def set_language(request, lang):
    if lang not in settings.MODELTRANSLATION_LANGUAGE:
        lang = settings.LANGUAGE_CODE

    activate(lang)
    host = request.build_absolute_uri('/')
    redirect_to = host + lang + request.META['HTTP_REFERER'].replace(host, '')[2:]
    return redirect(redirect_to)


def search(request):
    search = request.POST.get('search')
    request.session['search'] = search
    return redirect(request.META['HTTP_REFERER'])
