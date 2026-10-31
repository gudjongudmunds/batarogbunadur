from django import template

register = template.Library()

@register.filter
def to_percent(value):
    try:
        return f"{float(value) * 100:.1f}".replace('.', ',') + '%'
    except (ValueError, TypeError):
        return value

@register.filter
def format_number(value):
    try:
        # Format the number with a period as a thousand separator
        formatted_value = f"{int(value):,}".replace(",", ".")
        return f"{formatted_value},-"
    except (ValueError, TypeError):
        return value
    

@register.filter
def decimal_comma(value):
    try:
        return str(value).replace('.', ',')
    except (ValueError, TypeError):
        return value

# bunadur/templatetags/custom_filters.py

@register.filter(name='format_currency')
def format_currency(value):
    if value is None:
        return ''
    return f"{value:,.0f}".replace(',', '.') + ',-'

from django import template


@register.filter(name='floatformat')
def floatformat(value, arg):
    try:
        return round(float(value), int(arg))
    except (ValueError, TypeError):
        return value

@register.filter(name='div')
def div(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return None
