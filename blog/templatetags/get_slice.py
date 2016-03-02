from django.template import Library

register = Library()

@register.filter
def get_slice(value, i):
  if len(value) != 0:
    return value[4 * i : 4 * i + 4]
  else:
    return []