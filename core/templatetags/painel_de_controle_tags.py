from django import template
from core.models.painel_de_controle import PainelDeControleModel

register = template.Library()


@register.simple_tag()
def css_edit():
    return PainelDeControleModel.objects.first().css_editor


@register.simple_tag()
def logo_edit():
    return PainelDeControleModel.objects.first().logo


#
@register.simple_tag()
def font_edit():
    return PainelDeControleModel.objects.first().font_editor


@register.simple_tag()
def js_edit():
    return PainelDeControleModel.objects.first().js_editor
