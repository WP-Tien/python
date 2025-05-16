import uuid
import os
import re

import locale

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/images/product/', filename)

def get_skip_slug_article(path):
    # test/news/feeds-tang-lai-suat.html
    last_path = path.split('/')[-1]
    skip_slug = None;

    match = re.match(r'^(?P<article_slug>[\w-]+)-a\d+\.html$', last_path)

    if match:
        skip_slug = match.group('article_slug')

    return skip_slug

def format_currency_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    
    formatted_number = locale.format_string("%d", number, grouping=True) + "đ"
    
    return formatted_number