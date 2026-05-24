import re

VALID_INLINE_TAGS = (
    "area img object map param "
    "a abbr acronym dfn em strong "
    "code samp kbd var "
    "b i big small tt " # would like to leave these out :-)
    "span br bdo cite del ins q sub sup"
    # NB: deliberately leaving out iframe and script
).split()

value = '<b>Công ty</b> cung cấp bu lông ốc vít nhập khẩu chất lượng cao'

print( VALID_INLINE_TAGS )

def test( value, valid_tags ):
    pattern = r'\<(\s*/?\s*(%s))(.*?\s*)\>' % '|'.join(re.escape(tag) for tag in valid_tags)
    
    value = re.sub( pattern, '', value )
    
    print( value )

def test2( value, valid_tags ):
    if valid_tags:
        tag_re = re.compile(r'(?!\<\s*/?\s*(%s).*?\s*\>)\<(\s*/?\s*.*?)(.*?\s*)\>' % u'|'.join(re.escape(tag) for tag in valid_tags))     
    else:
        tag_re = re.compile('\<.*?\>')

    value = re.sub( tag_re, '', value )
    
    print(value)
    
test2(value, VALID_INLINE_TAGS)