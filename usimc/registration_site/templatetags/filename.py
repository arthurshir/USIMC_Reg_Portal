import os

from django import template


register = template.Library()

@register.filter
def filename(value):
	if not value:
		return value
    return os.path.basename(value.file.name)