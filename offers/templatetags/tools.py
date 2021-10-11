from django import template
from django.utils.safestring import mark_safe

from offers.models import Offer

register = template.Library()


@register.simple_tag
def unread_offers():
    unread_offers = Offer.objects.filter(is_readed=False)
    if unread_offers:
        return mark_safe(f'<span class="badge rounded-pill bg-danger align-self-end">{ unread_offers.count() }<span class="visually-hidden">unread messages</span></span>')
    return ""
