from django import template

register = template.Library()


@register.filter
def space(value):
    a=value.upper()
    return a

