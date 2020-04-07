from django.shortcuts import render
from .models import *


def products(request):
    product=Product.objects.all()
    return render(request, 'products/products_list.html', {'product':product})

def product(request, product_id):
    product=Product.objects.get(id=product_id)
    return render(request, 'products/product.html', {'product': product})

