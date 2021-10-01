from django import template

register = template.Library()

@register.filter()
def is_odd(value):
  return value % 2 == 1