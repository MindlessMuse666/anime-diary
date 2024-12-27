from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'slug'
    ]
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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