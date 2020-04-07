from django.shortcuts import render
from .models import Post
from products.models import *
from django.utils import timezone


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'mainpage/footer.html', {'posts': posts})


def mainpage(request):
    posts = Post.objects.all()
    products_images=ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_man_boot=products_images.filter(product__category__id=1)
    products_images_weman_boot=products_images.filter(product__category__id=2)
    return render(request, 'mainpage/main_page.html', {'products_images':products_images, 'posts':posts})





