from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books_api),
    path('cart/add/', views.add_to_cart_api),
]