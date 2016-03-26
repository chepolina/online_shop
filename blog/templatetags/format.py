from django.template import Library

register = Library()

@register.filter
def format( value):
    return value.replace(" ", "-").lower()
