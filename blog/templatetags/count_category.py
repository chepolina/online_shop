from django.template import Library
from blog.models import Product, Category

register = Library()

@register.filter
def count_category( value ):
  items = Product.objects.filter(category__name=value.name)
  return(len(items))