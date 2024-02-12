from django import template

register = template.Library()
# crea un decorador para poder registrar el filtro


@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    clase, valor = css.split(":")
    attrs[clase] = valor
    return field.as_widget(attrs=attrs)
