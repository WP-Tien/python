from django.urls import path, include, re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name='home'),
    path("<slug:post_slug>.html", views.page_template, name="posts"), 
    
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)