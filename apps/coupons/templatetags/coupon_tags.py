from decimal import Decimal

from django import template

register = template.Library()


@register.simple_tag
def multiply(cart_price, shipping_price):
    print(type(cart_price), type(shipping_price))
    return round((cart_price / 100) * shipping_price, 2)


@register.simple_tag
def add(value1,value2):
    return Decimal(value1) + value2
