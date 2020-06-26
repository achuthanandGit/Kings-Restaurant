from django import template
import re

register = template.Library()

@register.filter
def remove_white_space(value):
    return value.replace(" ","_")