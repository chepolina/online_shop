from django.template import Library

register = Library()

@register.filter
def get_category(f):
    return ['popular chocolate bar' ,
            'hoot chocolate on a spoon',
            'chocolate sets',
            'business gift',
            'luxury truffles']

