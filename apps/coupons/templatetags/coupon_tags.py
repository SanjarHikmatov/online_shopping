#
# from django import template
#
#
# register = template.Library()
#
# @register.simple_tag
# def decimal_to_range(cart_total_price_to: int, coupon_percentage: int):
#     print(type(cart_total_price_to), type(coupon_percentage), '>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
#     new_total = cart_total_price_to / coupon_percentage
#     return round(new_total, 2)
