from django import template

register = template.Library()

@register.simple_tag
def get_price_old(price, price_sale):
    return price if price_sale else ""