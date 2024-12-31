from django.shortcuts import HttpResponse, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def popular_list(request):
    products = Product.objects.filter(is_available = True)[:3]
    return render(
        request,
        'main/index/index.html',
        {'products': products}
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug = slug,
        is_available = True
    )

    return render(
        request,
        'main/product/detail.html',
        {'product': product}
    )


def product_list(request, category_slug = None):
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available = True)
    paginator = Paginator(products, 10)
    current_page = paginator.page(int(page))

    if category_slug:
        category = get_object_or_404(
            Category,
            slug = category_slug
        )
        paginator = Paginator(products.filter(category = category), 10)
        current_page = paginator.page(int(page))

    response: HttpResponse = render(
        request,
        'main/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products': current_page,
            'slug_url': category_slug
        }
    )
    
    return response