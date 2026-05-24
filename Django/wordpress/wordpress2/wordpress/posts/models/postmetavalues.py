from django.db import models

from .postmetakey import PostMetaKey

class PostMetaValues(models.Model):
    meta_id = models.ManyToManyField(PostMetaKey)
    meta_name = models.SlugField(unique=True, max_length=255)
    meta_value  = models.TextField()
    
    class Meta:
        db_table = "post_meta_values"
        verbose_name_plural = "Post Meta Values"
    
    def __str__(self):
        return self.meta_value