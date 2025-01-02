from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(
        Product,
        id=product_id
    )
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    
    target_redirect: HttpResponseRedirect = redirect('cart:cart_detail')

    return target_redirect


@require_POST
def cart_remove(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart.remove(product)

    target_redirect: HttpResponseRedirect = redirect('cart:cart_detail')

    return target_redirect


def cart_detail(request: HttpRequest):
    cart = Cart(request)

    render_view = render(
        request,
        'cart/detail.html',
        {'cart': cart}
    )

    return render_view