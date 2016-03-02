from django.template import Library
from math import ceil

register = Library()

@register.filter
def get_rows_range( value ):
  if len(value) != 0:
    return range( ceil(len(value) / 4) )
  else:
    return range(0)
