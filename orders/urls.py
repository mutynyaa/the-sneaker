from . import views
from django.urls import path

urlpatterns = [
    path('', views.orders, name='orders'),
    path('basket_adding/', views.basket_adding, name='basket_adding'),
]