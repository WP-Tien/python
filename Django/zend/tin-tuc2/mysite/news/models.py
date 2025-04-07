# from django.db import models
# from django.urls import reverse

# from tinymce.models import HTMLField

# from .helpers import *
# from .custom_field import *
# from .define import *

# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     # is_homepage = models.BooleanField(default=False)
#     is_homepage = CustomBooleanField()
#     layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICE, default=APP_VALUE_LAYOUT_DEFAULT)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
#     ordering = models.IntegerField(default=0)

#     class Meta:
#         verbose_name_plural = TABLE_CATEGORY_SHOW

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("category", kwargs={"category_slug": self.slug})

# class Article(models.Model):
#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
#     ordering = models.IntegerField(default=0)
#     # special = models.BooleanField(default=False)
#     special = CustomBooleanField()
#     publish_date = models.DateTimeField()
#     content = HTMLField()
#     # content = models.TextField()
#     image = models.ImageField(upload_to=get_file_path)

#     # Xoa Cate bai viet se~ bi xoa theo
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = TABLE_ARTICLE_SHOW

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("article", kwargs={"article_slug": self.slug, 'article_id': self.id})
    
# class Feed(models.Model):
#     name = models.CharField(unique=True, max_length=100)
#     slug = models.SlugField(unique=True, max_length=100)
#     status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
#     ordering = models.IntegerField(default=0)
#     link = models.CharField(max_length=250)

#     class Meta:
#         verbose_name_plural = TABLE_FEED_SHOW

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("feed", kwargs={"feed_slug": self.slug})

