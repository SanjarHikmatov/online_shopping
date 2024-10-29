# from decimal import Decimal
# import requests
# from django import template
# from apps.contact.forms import ContactForm
# from apps.users.models import CustomUser
#
# register = template.Library()
#
# @register.simple_tag
# def decimal_to_range(decimal_number):
#     return range(int(decimal_number))
#
# @register.simple_tag
# def username_equal_user(user_id: int, contact_id: int):
#     contact_form = ContactForm()
#     CustomUser.objects.filter(user_id=)
#     return
#
# @register.simple_tag
# def normalize_date(date_obj):
#     return date_obj.strftime('%m/%d/%Y')
#
# @register.simple_tag
# def product_in_wishlist(user_id: int, product_id: int) -> bool:
#     return Wishlist.objects.filter(user_id=user_id, product_id=product_id).exists()
#
#
#
# @register.simple_tag
# def get_price_by_currency(to_currency: str, price: Decimal) -> Decimal:
#     if to_currency == General.CurrencyChoices.UZS:
#         return price
#     return round(price / CurrencyAmount.get_currency(currency=to_currency),2)
#
#
#
#
