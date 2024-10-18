from apps.general.models import General, GeneralSocialMedia


def general_context(request):
    context = {
        'general': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', General.DEFAULT_CURRENCY),
        'currency_list': General.CurrencyChoices.labels,
    }
    return context