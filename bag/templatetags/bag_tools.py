from django import template

register = template.Library()

@register.filter(name='calc_subtotal')

def calc_subtotal(price, num_of_weeks):
    return price * num_of_weeks