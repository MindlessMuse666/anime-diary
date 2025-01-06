from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe


class OrderItemInLine(TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def order_stripe_payment(obj):
    url = obj.get_stripe_url()
    
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        
        return mark_safe(html)

    return ''
order_stripe_payment.short_description = 'Stripe payment'


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
        order_stripe_payment,
        'created',
        'updated'
    ]
    list_filter = [
        'is_paid',
        'created',
        'updated'
    ]
    inlines = [OrderItemInLine]