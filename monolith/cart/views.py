from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Import cái này
from .models import Cart, CartItem
from books.models import Book

# Thêm @login_required để bắt buộc phải đăng nhập mới xem được giỏ
@login_required(login_url='login')
def view_cart(request):
    # Dùng request.user.id thay vì số 1
    cart, created = Cart.objects.get_or_create(customer_id=request.user.id)
    items = cart.items.all() # Hoặc .cartitem_set.all() tùy code của bạn
    total_price = sum(item.book.price * item.quantity for item in items)
    
    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total_price': total_price
    })

@login_required(login_url='login')
def add_to_cart(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        # Dùng request.user.id thay vì số 1
        cart, created = Cart.objects.get_or_create(customer_id=request.user.id)
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('view_cart')
    return redirect('book_list')