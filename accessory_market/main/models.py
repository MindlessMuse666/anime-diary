from django.db.models import (Model, Index, ForeignKey, CASCADE,
        CharField, SlugField, ImageField, TextField, 
        BooleanField, DateTimeField, DecimalField) 
from django.urls import reverse


class Category(Model):
    name = CharField(
        max_length=20,
        unique=True
    )
    slug = SlugField(
        max_length=20,
        unique=True
    )


    def get_absolute_url(self):
        return reverse(
            "main:product_list_by_category",
            args=[self.slug]
        )
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(Model):
    category = ForeignKey(
        Category,
        related_name='products',
        on_delete=CASCADE
    )
    name = CharField(max_length=50)
    slug = SlugField(max_length=50)
    image = ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    description = TextField(blank=True)
    price = DecimalField(
        max_digits=10,
        decimal_places=2
    )
    is_available = BooleanField(
        default=True
    )
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    discount = DecimalField(
        default=.00,
        max_digits=4,
        decimal_places=2
    )


    class Meta:
        ordering = ['name']
        indexes = [
            Index(fields=['id', 'slug']),
            Index(fields=['name']),
            Index(fields=['-created']),
        ]

    
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse(
            'main:product_detail',
            args=[self.slug]
        )
    

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
    
    
class ProductImage(Model):
    product = ForeignKey(
        Product,
        related_name='images',
        on_delete=CASCADE
    )
    image = ImageField(
        upload_to='product/%Y/%m/%d',
        blank=True
    )
    
    
    def __str__(self):
        return f'{self.product.name} - {self.image.name}'