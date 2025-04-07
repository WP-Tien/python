import re
import feedparser
from bs4 import BeautifulSoup

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 
from django.utils import timezone

from .models import Category, Article, Feed
from .define import *

def index(request):
    items_article_special = Article.objects.filter(special=True, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by('ordering')

    for category in items_category:
        category.article_filter  = category.article_set.filter(status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    context = {
        'title_page': "Trang chủ",
        'items_article_special': items_article_special,
        'items_category': items_category
    }

    # dd(context)

    return render(request, APP_PATH_PAGES + 'index.html', context)

def category(request, category_slug):
    # category_slug => thong tin category => article thuoc category => do du lieu ra phi client
    item_category = get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)
    items_article = Article.objects.filter(category=item_category, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    # Pagination
    post_per_pages = SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE
    page = request.GET.get('page')

    paginator = Paginator( items_article, post_per_pages )

    items_article = paginator.get_page(page)
    # End pagination

    context = {
        'title_page': item_category.name,
        'item_category': item_category,
        'items_article': items_article,
        'paginator': paginator
    }

    return render(request, APP_PATH_PAGES + 'category.html', context)

def article(request, article_slug, article_id):
    item_article = get_object_or_404(Article, id=article_id, slug=article_slug, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now())

    items_related_article = Article.objects.filter(category=item_article.category, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date').exclude(id__in=[item_article.id])[:SETTING_ARTICLE_TOTAL_ITEMS_RELATED]

    context = {
        'title_page': item_article.name,
        'item_article': item_article,
        'items_related_article': items_related_article
    }

    # dd(items_related_article)

    return render(request, APP_PATH_PAGES + 'article.html', context)

def feed(request, feed_slug):
    item_feed = get_object_or_404(Feed, slug=feed_slug, status=APP_VALUE_STATUS_ACTIVE)

    items_feed = []

    try: 
        feed = feedparser.parse(item_feed.link)

        for entry in feed.entries:
            soup = BeautifulSoup(entry.summary, 'html.parser')
            img_tag = soup.find('img')
            src_img = APP_VALUE_IMAGE_DEFAULT

            if img_tag:
                src_img = img_tag['src']

            item = {
                'title': entry.title,
                'link': entry.link,
                'pub_date': entry.published,
                'img': src_img
            }

            items_feed.append(item)

        context = {
            'title_page': "Tin tức tổng hợp " + item_feed.name,
            'item_feed': item_feed,
            'items_feed': items_feed
        }

        # dd(item_feed)
    except:
        print("Get Feed: Error!")

    return render(request, APP_PATH_PAGES + 'feed.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    """
        contains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể.
        icontains: Tìm kiếm các giá trị có chứa một chuỗi con cụ thể (không phân biệt chữ hoa/ chữ thường).
        regex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể.
        iregex: Tìm kiếm các giá trị phù hợp với một biểu thức chính quy cụ thể (không phân biệt chữ hoa/ chữ thường).
    """
    items_article = Article.objects.filter(name__iregex=re.escape(keyword), status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    # Pagination
    post_per_pages = SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE
    page = request.GET.get('page')

    paginator = Paginator( items_article, post_per_pages )

    items_article = paginator.get_page(page)
    # End pagination

    context = {
        'title_page': "Tìm kiếm từ khoá: " + keyword,
        'items_article': items_article,
        'keyword' : keyword,
        'paginator': paginator
    }

    # dd(context)

    return render(request, APP_PATH_PAGES + 'search.html', context)

def about(request):

    return render(request, APP_PATH_PAGES + 'about.html', {
        "title_page": "Giới thiệu"
    })

def contact(request):

    return render(request, APP_PATH_PAGES + 'contact.html', {
        "title_page": "Liên hệ"
    })