from django.template import Library
from blog.models import Product

register = Library()

@register.filter
def count_category( value, category):
  items = Product.objects.filter(category=category)
  return(len(items))