from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from books.models import Book
import json

# Tắt kiểm tra CSRF để test API cho dễ (thực tế không nên)
@csrf_exempt 
def add_to_cart(request):
    if request.method == 'POST':
        # Giả lập user đã đăng nhập (vì ta chưa làm login ở frontend)
        # Lấy user đầu tiên trong database để test
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.first() 
        
        if not user:
            return JsonResponse({'error': 'Chua co user nao, hay tao superuser truoc!'}, status=400)

        # Lấy dữ liệu gửi lên
        try:
            data = json.loads(request.body)
            book_id = data.get('book_id')
            quantity = data.get('quantity', 1)
        except:
            return JsonResponse({'error': 'Du lieu khong hop le'}, status=400)

        # Lấy hoặc tạo Giỏ hàng cho user này
        cart, created = Cart.objects.get_or_create(customer=user)

        # Kiểm tra sách có tồn tại không
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Sach khong ton tai'}, status=404)

        # Thêm vào giỏ
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        return JsonResponse({'message': 'Da them vao gio hang thanh cong!', 'cart_id': cart.id})
    
    return JsonResponse({'error': 'Phai dung phuong thuc POST'}, status=405)