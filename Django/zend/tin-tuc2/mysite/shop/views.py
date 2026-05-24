from django.shortcuts import render, get_object_or_404
from .define import *
from .models import *
from .helpers import *

# Create your views here.
def index(request):    
    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by('ordering')

    for category in items_category:
        category.product_filter = category.product_set.filter(status=APP_VALUE_STATUS_ACTIVE).order_by('ordering')[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    items_product_latest = Product.objects.filter( status=APP_VALUE_STATUS_ACTIVE).order_by('-id')[:SETTING_PRODUCT_TOTAL_ITEMS_LATEST_INDEX]
    items_product_latest = chunked(items_product_latest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)
    
    items_product_hot = Product.objects.filter( status=APP_VALUE_STATUS_ACTIVE).order_by('-total_sold')[:SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX]
    items_product_hot = chunked(items_product_hot, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)
    
    items_product_random = Product.objects.filter( status=APP_VALUE_STATUS_ACTIVE).order_by('?')[:SETTING_PRODUCT_TOTAL_ITEMS_RANDOM_INDEX]
    items_product_random = chunked(items_product_random, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    context = {
        'title_page': "Trang chủ",
        'items_category': items_category,
        'items_product_latest': items_product_latest,
        'items_product_random': items_product_random,
        'items_product_hot': items_product_hot
    }

    # dd(context)

    return render(request, APP_PATH_PAGES + 'index.html', context)

def product(request, product_slug, product_id):
    item_product = get_object_or_404(Product, id=product_id, slug=product_slug, status=APP_VALUE_STATUS_ACTIVE)

    items_related_product = Product.objects.filter(category=item_product.category, status=APP_VALUE_STATUS_ACTIVE).order_by('-id').exclude(slug=product_slug)[:SETTING_PRODUCT_TOTAL_ITEMS_RELATED]

    context = {
        'title_page' : item_product.name,
        'item_product' : item_product,
        'items_related_product': items_related_product
    }

    return render(request, APP_PATH_PAGES + 'detail.html', context)