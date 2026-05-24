from django.db import models
from django.core.exceptions import ValidationError

from .posts import Posts

class PostMetaKey(models.Model):
    post_id     = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
    meta_key    = models.SlugField(unique=True, max_length=255)    
    
    class Meta:
        db_table = "post_meta_key"
        verbose_name_plural = "Post Meta Key"
        unique_together = ['post_id', 'meta_key'] # optional
    
    def __str__(self):
        return self.meta_key
    
    def clean(self):
        # Custom validations
        if self.post_id.post_type != "page":
            raise ValidationError("Error")
        
    def save(self, *args, **kwargs):
        self.full_clean() # run the validators
        super().save(*args, **kwargs)