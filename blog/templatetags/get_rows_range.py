from django.template import Library
from math import ceil

register = Library()

@register.filter
def get_rows_range( value ):
  return range( ceil(len(value) / 4) )
