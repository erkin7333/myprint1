from myprint.models import MetaDescription
from django import template
from django.template.loader import get_template


register = template.Library()
@register.filter()
def meta_description(category):
    return MetaDescription.objects.filter(category_id=category)