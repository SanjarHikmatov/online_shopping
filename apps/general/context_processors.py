from apps.general.models import General, GeneralSocialMedia
from apps.categories.models import Category
from apps.products.models import Product


def general_context(request):
    context = {
        'categories': Category.objects.prefetch_related('children','products').filter(parent__isnull=True),
        'general': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', General.DEFAULT_CURRENCY),
        'currency_list': General.CurrencyChoices.labels,
        'products': Product.objects.all().order_by('-id')[0:12],

    }
    return context