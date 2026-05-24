from django.contrib import admin
from django.utils.html import mark_safe

from .models import Posts, PostMetaKey, PostMetaValues
from .define import *

class PostMetaInline(admin.TabularInline):
    model = PostMetaKey
    fields = ["meta_key"]
    readonly_fields = ["meta_key"]
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True

class PostsAdmin(admin.ModelAdmin):
    list_display = ( 'image_tag', 'post_title', 'post_slug', 'post_status', 'post_type', 'created_date')

    list_filter = ["post_status", "post_type"]
    search_fields = ["post_title"]
    
    inlines = [PostMetaInline]
    
    def image_tag(self, obj):
        src_img = ADMIN_NO_IMG
        
        if obj.post_image:
            src_img = obj.post_image
        
        return mark_safe('<img src="/static/%s" style="object-fit: cover;" width="100" height="100" />' % (src_img))
    
    image_tag.short_description = 'Image display'
    image_tag.allow_tags = True
    
    # fields = ('image_tag', )
    readonly_fields = ('image_tag', )

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS
    
class PostMetaKeyInline(admin.TabularInline):
    model = PostMetaValues.meta_id.through
    fields = ['meta_value']
    readonly_fields = ['meta_value']
    can_delete = False
    max_num = 0
    extra = 0
    show_change_link = True
    
    def meta_value(self, instance):
        return instance.postmetavalues.meta_value
    
    meta_value.short_description = 'Key value'
    
class PostMetaKeyAdmin(admin.ModelAdmin):
    list_display = ('meta_key', )
    
    list_filter = ["post_id"]
    search_fields = ["meta_key"]
    
    inlines = [PostMetaKeyInline]
    
    def render_change_form(self, request, context, *args, **kwargs):
        # Filter post = page
        context['adminform'].form.fields['post_id'].queryset = Posts.objects.filter(post_type__iexact='page')
        return super(PostMetaKeyAdmin, self).render_change_form(request, context, *args, **kwargs)
    
class PostMetaValuesAdmin(admin.ModelAdmin):
    list_display = ('meta_value', )
    
    list_filter = ["meta_value"]
    search_fields = ["meta_value"]
    
admin.site.register(PostMetaKey, PostMetaKeyAdmin)
admin.site.register(PostMetaValues, PostMetaValuesAdmin)

admin.site.register(Posts, PostsAdmin)