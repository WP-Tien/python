import uuid
import os
import re

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/article/', filename)

def get_skip_slug_article(path):
    # test/news/feeds-tang-lai-suat.html
    last_path = path.split('/')[-1]
    skip_slug = None;

    match = re.match(r'^(?P<article_slug>[\w-]+)-a\d+\.html$', last_path)

    if match:
        skip_slug = match.group('article_slug')

    return skip_slug