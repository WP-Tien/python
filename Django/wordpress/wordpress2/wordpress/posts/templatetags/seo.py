from django import template
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from ..models import Posts 
from ..helpers import * 
from ..define import *

register = template.Library()

@register.simple_tag 
def title_tag(post_slug): 
    """
        render <title> value </title> tag
    """
    tag_name = 'title'    
    
    if post_slug:
        post = get_object_or_404(Posts, post_slug=post_slug, post_status='published')
    else:
        post = get_object_or_404(Posts, post_slug='home', post_status='published')

    value = post.seo_title if post.seo_title is not None else post.post_title

    # clean value
    value = remove_invalid_tags(value, VALID_INLINE_TAGS)
    value = value.strip()

    html = "<%s>%s</%s>" % (tag_name, value, tag_name)

    return mark_safe(html)

@register.simple_tag 
def description_meta(post_slug):
    """
        render <meta name="description" content="My description" /> tag
    """
    meta_name = 'description'    

    if post_slug:
        post = get_object_or_404(Posts, post_slug=post_slug, post_status='published')
    else:
        post = get_object_or_404(Posts, post_slug='home', post_status='published')
        
    value = post.seo_description if post.seo_description is not None else ''
    
    # clean value
    value = remove_invalid_tags(value, None)
    value = value.replace("\n", " ").strip()
    
    html = '<meta name="%s" content="%s">' % (meta_name, value)
    
    return mark_safe(html)

@register.simple_tag 
def keywords_meta(post_slug):
    """
        render <meta name="keywords" content="My, list, of, keywords" /> tag
    """
    meta_name = 'keywords'
    if post_slug:
        post = get_object_or_404(Posts, post_slug=post_slug, post_status='published')
    else:
        post = get_object_or_404(Posts, post_slug='home', post_status='published')
        
    value = post.seo_keyword if post.seo_keyword is not None else ''

    # clean value
    value = remove_invalid_tags(value, None)
    value = value.replace('"', '&#34;').replace("\n", ", ").strip()
    
    html = '<meta name="%s" content="%s">' % (meta_name, value)

    return mark_safe(html)

@register.simple_tag
def og_meta_title(post_slug):
    """
        render <meta property="og:title" content="The Rock (1996) ⭐ 7.4 | Action, Adventure, Thriller">
    """
    property_name = 'og:title'
    if post_slug:
        post = get_object_or_404(Posts, post_slug=post_slug, post_status='published')
    else:
        post = get_object_or_404(Posts, post_slug='home', post_status='published')
        
    value = post.og_title if post.og_title is not None else ''
    
    # clean value
    value = remove_invalid_tags(value, VALID_INLINE_TAGS)
    value = value.strip()
    
    html = '<meta property="%s" content="%s">' % (property_name, value)
    
    return mark_safe(html)

@register.simple_tag 
def og_meta_description(post_slug):
    """
        render <meta property="og:description" content="2h 16m | R">
    """
    property_name = 'og:description'
    if post_slug:
        post = get_object_or_404(Posts, post_slug=post_slug, post_status='published')
    else:
        post = get_object_or_404(Posts, post_slug='home', post_status='published')
        
    value = post.og_description if post.og_description is not None else ''
    
    # clean value 
    value = remove_invalid_tags(value, VALID_INLINE_TAGS)
    value = value.replace("\n", " ").strip()
    
    html = '<meta property="%s" content="%s">' % (property_name, value)
    
    return mark_safe(html)