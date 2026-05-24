"""
MODEL
"""
WORDPRESS_STATUS_POSTS_CHOICES = (
    ('draft', 'Draft'),
    ('pending', 'Pending'),
    ('published', 'Published')
)
WORDPRESS_STATUS_POSTS_DEFAULT = "draft"

WORDPRESS_POST_TYPE_CHOICES = (
    ('post', 'Post'),
    ('page', 'Page'),
    ('menu', 'Menu'),
)
WORDPRESS_POST_TYPE_DEFAULT = "post"


"""
ADMIN
"""
ADMIN_SRC_JS = ('wordpress_admin/js/jquery-3.6.0.min.js', 'wordpress_admin/js/slugify.min.js', 'wordpress_admin/js/general.js')
ADMIN_SRC_CSS = {'all': ('wordpress_admin/css/custom.css',)}
ADMIN_NO_IMG = '/wordpress_admin/images/posts/no-image.jpg';

"""
HELPER
"""
VALID_INLINE_TAGS = (
    "area img object map param "
    "a abbr acronym dfn em strong "
    "code samp kbd var "
    "b i big small tt "
    "span br bdo cite del ins q sub sup"
).split()