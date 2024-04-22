from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):

    """ View to return the all products page, including sorting and search functionality """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    """ View to return the the page for individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
