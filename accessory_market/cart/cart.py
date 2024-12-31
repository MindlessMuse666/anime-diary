from decimal import Decimal
from django.conf import settings
from django.db.models.manager import BaseManager
from django.http.request import HttpRequest
from main.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session(settings.CART_SESSION_ID) = {}
        
        self.cart = cart
    

    def add(self, product: Product, quantity: int = 1, override_quantity: bool = False):
        product_id: str = str(product.id) 

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    
    def save(self):
        self.session.modified = True
    

    def remove(self, product: Product):
        product_id: str = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    

    def __iter__(self):
        product_ids = self.cart.keys()
        products: BaseManager[Product] = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item
    

    def __len__(self):
        summary = sum(item['quantity'] for item in self.cart.values())

        return summary
    

    def clear(self):
        del self.session[settings.CART_SESSION_ID]