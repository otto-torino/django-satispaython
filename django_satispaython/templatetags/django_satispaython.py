from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag('django_satispaython/satispay_button.html')
def satispay_button(payment_id):
    return { 'payment_id': payment_id, 'staging': settings.SATISPAYTHON_STAGING }