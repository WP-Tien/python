from django.shortcuts import render, get_object_or_404

from .models import Posts, PostMetaKey
from .define import *

def home(request):
    # post = get_object_or_404(Posts, post_slug='home', post_status='published', post_type='page')
    # items_post_meta = PostMeta.objects.filter(post_id=post)
    
    context = {
        'items_post_meta': 'test'
    }
     
    return render(request, 'page_template/home.html', context)
    
def page_template(request, post_slug):
    post = get_object_or_404(Posts, post_slug=post_slug, post_status='published', post_type='page')
    items_post_meta = PostMetaKey.objects.filter(post_id=post)
         
    context = {
        'items_post_meta': items_post_meta
    }
    
    # match post_slug:
    #     case 'contact':
    #         return render(request, 'page_template/contact.html', context)
    #     case 'about':
    #         return render(request, 'page_template/about.html', context)
    #     case _:
    #         return render(request, 'page_template/default.html', context)
    
    if post_slug == 'contact':
        return render(request, 'page_template/contact.html', context)
    elif post_slug == 'about':
        return render(request, 'page_template/about.html', context)
    else:
        return render(request, 'page_template/default.html', context)