from django.template import Library

register = Library()

@register.filter
def get_category(f):
    return ['popular chocolate bar' ,
            'hot chocolate on a spoon',
            'chocolate sets',
            'business gifts',
            'luxury truffles']

