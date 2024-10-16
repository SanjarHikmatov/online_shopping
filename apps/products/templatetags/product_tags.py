from django import template

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