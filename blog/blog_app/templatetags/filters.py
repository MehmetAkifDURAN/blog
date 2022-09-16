from django import template

register = template.Library()


@register.filter
def text_clip(text, length):
    if len(text) > length:
        return text[:length] + '...'

    return text
