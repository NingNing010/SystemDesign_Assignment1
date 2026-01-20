"""
URL configuration for ninh_proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books.views import book_list
from cart.views import view_cart, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Trang chủ là danh sách sách
    path('', book_list, name='home'), 
    path('books/', book_list, name='book_list'),
    
    # URL cho giỏ hàng
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
]