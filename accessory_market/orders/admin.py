from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Order, OrderItem


class OrderItemInLine(TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'address',
        'postal_code',
        'city',
        'is_paid',
        'created',
        'updated'
    ]
    list_filter = [
        'is_paid',
        'created',
        'updated'
    ]
    inlines = [OrderItemInLine]