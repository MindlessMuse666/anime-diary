from django.http.request import HttpRequest
from .cart import Cart


def cart(request: HttpRequest) -> dict:
    """Контекст процессора"""
    cart_context_dict: dict = {'cart': Cart(request)}

    return cart_context_dict