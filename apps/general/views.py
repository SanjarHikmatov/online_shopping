from django.shortcuts import redirect, render
from django.conf import settings
from django.utils.translation import activate

from apps.products.models import CurrencyChoices


def set_language(request, lang):
    if lang not in settings.MODELTRANSLATION_LANGUAGE:
        lang = settings.LANGUAGE_CODE

    activate(lang)
    host = request.build_absolute_uri('/')
    redirect_to = host + lang + request.META['HTTP_REFERER'].replace(host, '')[2:]
    return redirect(redirect_to)


def set_currency(request, currency):
    currencies = CurrencyChoices.values
    if currency in currencies:
        request.session['currency'] = currency
    return redirect(request.META['HTTP_REFERER'])

def search(request):
    search_text = request.GET.get('search', '')
    request.session['search_text'] = search_text
    return redirect('products:product_list')
