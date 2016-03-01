from django.template import Library

register = Library()

@register.filter
def get_slice(value, i):
  return value[4 * i : 4 * i + 4]