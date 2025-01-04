from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request: HttpRequest):
    cart = Cart(request)
    render_view: HttpResponse

    if request.method == 'POST':
        form = OrderCreateForm(
            request.POST,
            request=request
        )

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            cart.clear()

            render_view = render(
                request,
                'order/created.html',
                {
                    'order': order,
                    'form': form
                }
            )

            return render_view
    else:
        form = OrderCreateForm(request=request)
        render_view = render(
            request,
            'order/create.html',
            {
                'cart': cart,
                'form': form
            }
        )

        return render_view