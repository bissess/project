from django import template
from ..models import PostCategory


register = template.Library()


@register.inclusion_tag('autoblog/list_categories.html')
def show_categories():
    categories = PostCategory.objects.all()
    return {'categories': categories}