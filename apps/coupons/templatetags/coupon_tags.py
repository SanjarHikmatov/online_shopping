
from django import template
from django.db.models.expressions import NoneType

register = template.Library()


@register.simple_tag
def multiply(total_cart_price, shipping):
    return round((total_cart_price // 100) * shipping, 2)

@register.simple_tag
def add(shipping, total_cart_price):
    return shipping + total_cart_price

@register.simple_tag
def minus(total_cart_price, discount_percent_coupon):
    return total_cart_price - discount_percent_coupon
