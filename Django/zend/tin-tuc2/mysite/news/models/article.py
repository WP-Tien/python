from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from news.helpers import *
from news.custom_field import *
from news.define import *
from .category import Category

class Article(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    # special = models.BooleanField(default=False)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    # content = models.TextField()
    image = models.ImageField(upload_to=get_file_path)

    # Xoa Cate bai viet se~ bi xoa theo
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = TABLE_ARTICLE_SHOW

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article", kwargs={"article_slug": self.slug, 'article_id': self.id})