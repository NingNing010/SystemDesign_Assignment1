from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from books.models import Book

# 1. Xem giỏ hàng
def view_cart(request):
    # Lấy giỏ hàng của khách ID=1 (Mặc định cho demo)
    cart, created = Cart.objects.get_or_create(customer_id=1)
    items = cart.items.all()
    
    # Tính tổng tiền
    total_price = sum(item.book.price * item.quantity for item in items)
    
    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total_price': total_price
    })

# 2. Thêm vào giỏ (Xử lý logic xong quay lại trang chủ)
def add_to_cart(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        cart, created = Cart.objects.get_or_create(customer_id=1)
        
        # Kiểm tra xem sách đã có trong giỏ chưa
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('view_cart') # Thêm xong chuyển hướng đến trang giỏ hàng
    return redirect('book_list')