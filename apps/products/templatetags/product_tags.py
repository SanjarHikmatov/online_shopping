from django import template

register = template.Library()

@register.simple_tag
def decimal_to_range(decimal_number):
    return range(int(decimal_number))



@register.simple_tag
def normalize_date(date_obj):
    return date_obj.strftime('%m/%d/%Y')