import uuid
import os
import re

# from django.utils.safestring import mark_safe
# from django.utils.html import conditional_escape

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('posts/images/posts/', filename)

# def _replace_quot(match):
#     unescape = lambda v: v.replace('&quot;', '"').replace('&amp;', '&')
#     return u'<%s%s>' % (unescape(match.group(1)), unescape(match.group(3)))

# def escape_tags(value, valid_tags):
#     # 1. escape everything
#     value = conditional_escape(value)
    
#     # 2. Có thể kích hoạt lại tags hiện tại
#     if valid_tags:
#         tag_re = re.compile(r'\<(\s*/?\s*(%s))(.*?\s*)\>' % u'|'.join(re.escape(tag) for tag in valid_tags))
        
#         value = tag_re.sub(_replace_quot, value)
        
#     # Allow comments to be hidden
#     value = value.replace("&lt;!--", "<!--").replace("--&gt;", "-->")
    
#     return mark_safe(value)

def remove_invalid_tags(value, valid_tags):    
    """ Xoá những tags không cần thiết
        ?! là phủ định

    Args:
        value (string): Giá trị càn xoá tag
        valid_tags (list): Những tags hợp lệ cho phép xuất hiện
    """
    
    if valid_tags:
        tag_re = re.compile(r'(?!\<\s*/?\s*(%s).*?\s*\>)\<(\s*/?\s*.*?)(.*?\s*)\>' % u'|'.join(re.escape(tag) for tag in valid_tags))
    else:
        tag_re = re.compile('\<.*?\>')

    value = re.sub( tag_re, '', value )
    
    return value