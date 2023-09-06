from django import template

from ..models import FeedBack

register = template.Library()

@register.inclusion_tag("reviews_page.html", takes_context=True)
def get_the_latest_five_reviews(context):
    reviews = FeedBack.objects.order_by('-date_submitted')[:5]
    context['reviews'] = reviews
    return context
