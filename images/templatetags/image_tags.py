
from django import template

register = template.Library()

@register.simple_tag
def get_sized_image(object, size=None):
    return object.get_sized_image(size)
