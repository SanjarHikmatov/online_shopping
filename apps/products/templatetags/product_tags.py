from decimal import Decimal

from django import template

from apps.general.models import CurrencyAmount
from apps.wishlists.models import Wishlist

register = template.Library()

@register.simple_tag
def decimal_to_range(decimal_number):
    return range(int(decimal_number))



@register.simple_tag
def normalize_date(date_obj):
    return date_obj.strftime('%m/%d/%Y')

@register.simple_tag
def product_in_wishlist(user_id: int, product_id: int) -> bool:
    return Wishlist.objects.filter(user_id=user_id, product_id=product_id).exists()



@register.simple_tag
def get_price_by_currency(to_currency: str, price: Decimal) -> Decimal:
    return round(CurrencyAmount.get_currency(currency=to_currency) / price, 2)




