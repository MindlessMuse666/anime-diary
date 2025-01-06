from django.contrib.admin import ModelAdmin, TabularInline, register 
from .models import Product, Category, ProductImage


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [
        'name', 
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 5
    

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = [
        'name',
        'slug',
        'price',
        'is_available',
        'created',
        'updated',
        'discount'
    ]
    list_filter = [
        'is_available',
        'created',
        'updated'
    ]
    list_editable = [
        'price',
        'is_available',
        'discount'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ProductImageInline]