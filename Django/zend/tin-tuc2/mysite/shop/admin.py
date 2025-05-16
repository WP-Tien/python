from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Category, Product, PlantingMethod, Contact

from .define import *
from .helpers import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'ordering')
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ['is_homepage', "status"]
    search_fields = ["name"]

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class ProductAdmin(admin.ModelAdmin):
    list_display = ('display_image', 'name', 'status', 'ordering', 'category', 'special', 'price_formatted', 'price_sale_formatted', 'price_real', 'get_planting_methods', 'total_sold')
    
    list_filter = ["status", "special", "planting_methods"]
    search_fields = ["name"]
    
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS
        
    @admin.display(description="Planting Methods")
    def get_planting_methods(self, obj):
        methods = [ method.name for method in obj.planting_methods.all() ]
        return ', '.join(methods)
    # get_planting_methods.short_description = 'Planting Methods'
    
    @admin.display(description="Price")
    def price_formatted(self, obj):
        return format_currency_vietnam(obj.price) if obj.price else obj.price
    
    @admin.display(description="Price sale")
    def price_sale_formatted(self, obj):
        return format_currency_vietnam(obj.price_sale) if obj.price_sale else obj.price_sale
    
    @admin.display(description="Image")
    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    
class PlantingMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering')
    list_filter = ["status"]
    search_fields = ["name"]
    
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone', 'message', 'created')
    fields = ('name', 'email', 'phone', 'created', 'message', 'contacted', 'message_admin')
    list_display = ('name', 'email', 'phone', 'created', 'contacted', 'message', 'message_admin')
    list_filter = ["contacted"]
    search_fields = ["name"]
    
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    def has_add_permission(self, request):
        return False

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PlantingMethod, PlantingMethodAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.site_header = ADMIN_HEADER_NAME