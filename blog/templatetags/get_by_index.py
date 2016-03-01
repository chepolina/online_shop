from django.template import Library

register = Library()

@register.filter
def get_by_index( value, i):
  return [value[i]]
