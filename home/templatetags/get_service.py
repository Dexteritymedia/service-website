from django import template

from ..models import ServicePage

register = template.Library()

@register.inclusion_tag("service_homepage.html", takes_context=True)
def get_service(context):
    services = ServicePage.objects.live().public().order_by('-first_published_at')[:6]
    context['services'] = services
    return context
