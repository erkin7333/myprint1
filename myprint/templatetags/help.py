from django.template.defaultfilters import register
from myprint.models import MetaDescription

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


