from django.utils import timezone
from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from posts.helpers import *
from posts.define import *

class Posts(models.Model):
    post_title      = models.CharField(unique=True, max_length=255)
    post_slug       = models.SlugField(unique=True, max_length=255, default=None)
    post_content    = HTMLField(blank=True)
    post_excerpt    = models.TextField(blank=True)
    post_status     = models.CharField(max_length=20, choices=WORDPRESS_STATUS_POSTS_CHOICES, default=WORDPRESS_STATUS_POSTS_DEFAULT)
    post_parent     = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    post_type       = models.CharField(max_length=20, choices=WORDPRESS_POST_TYPE_CHOICES, default=0)
    post_date       = models.DateTimeField()
    created_date    = models.DateTimeField(default=timezone.now)
    published_date  = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    post_image      = models.ImageField(blank=True, upload_to=get_file_path, null=True)
    
    # For SEO
    seo_title       = models.CharField(blank=True, unique=True, max_length=255, help_text="This is the page title, that appers in the title bar.")
    seo_keyword     = models.CharField(blank=True, unique=True, max_length=255, help_text="Comma-separated keywords for search engines.")
    seo_description = models.TextField(blank=True, unique=True, max_length=255, help_text="A short description, displayed in search results.")
    
    # Adding some fields for facebook (opengraph)
    og_title        = models.CharField(blank=True, unique=True, max_length=255)
    og_description  = models.TextField(blank=True, unique=True, max_length=255)
    
    class Meta:
        db_table = "posts"
        verbose_name_plural = "Posts"
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.post_title
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"post_slug": self.slug})