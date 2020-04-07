from . import views
from django.urls import path

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:product_id>/', views.product, name='product')
]