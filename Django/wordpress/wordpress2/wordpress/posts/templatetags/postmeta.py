from django import template
from ..models import Posts, PostMetaKey

register = template.Library()

# @register.simple_tag
# def get_meta(key):
#     try:
#         return PostMeta.objects.get(
#             meta_key=key
#         ).meta_value
#     except PostMeta.DoesNotExist:
#         return None