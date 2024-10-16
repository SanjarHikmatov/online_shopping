from apps.categories.models import Category
from apps.general.models import General, GeneralSocialMedia
from apps.products.models import Product, CurrencyChoices
from apps.wishlists.models import Wishlist


def general_context(request):
    context = {
        'general': General.objects.all(),
        'general_social_media': GeneralSocialMedia.objects.all(),
        'currency': request.session.get('currency', Product.DEFAULT_CURRENCY),
        'currency_list': CurrencyChoices.labels,
    }
    return context