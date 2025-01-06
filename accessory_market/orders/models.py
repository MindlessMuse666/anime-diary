from django.db.models import (Model, ForeignKey, 
                              CharField, BooleanField, DecimalField, PositiveIntegerField,
                              EmailField, DateTimeField, 
                              SET_DEFAULT, CASCADE, 
                              Index)
from django.conf import settings
from main.models import Product
from users.models import User


class Order(Model):
    user = ForeignKey(
        to=User,
        on_delete=SET_DEFAULT,
        blank=True,
        null=True,
        default=None
    )
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    email = EmailField()
    city = CharField(max_length=100)
    address = CharField(max_length=250)
    postal_code = CharField(max_length=20)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    is_paid = BooleanField(default=False)
    stripe_id = CharField(max_length=250, blank=True)


    class Meta:
        ordering = ['-created']
        indexes = [
            Index(fields=['-created'])
        ]
    

    def __str__(self):
        return f'Order {self.id}'
    

    def get_total_price(self):
        total_price = sum(item.get_price() for item in self.items.all())

        return total_price
    
    
    def get_stripe_url(self):
        if not self.stripe_id:
            return ''
        
        if '_test_' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        else:
            path = '/'
        
        return f'https://dashboard.stripe.com{path}payment/{self.stripe_id}'


class OrderItem(Model):
    order = ForeignKey(
        Order,
        related_name='items',
        on_delete=CASCADE,
    )
    product = ForeignKey(
        Product,
        related_name='order_items',
        on_delete=CASCADE
    )
    price = DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)
    

    def get_price(self):
        return self.price * self.quantity