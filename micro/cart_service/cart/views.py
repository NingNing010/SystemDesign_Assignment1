import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book_id = data.get('book_id')
        customer_id = data.get('customer_id')
        quantity = data.get('quantity', 1)

        # BƯỚC 1: GỌI SANG BOOK SERVICE (8001) ĐỂ KIỂM TRA SÁCH
        # (Giả lập giao tiếp giữa các services)
        try:
            response = requests.get('http://127.0.0.1:8001/api/books/list/')
            books = response.json().get('books', [])
            
            # Tìm xem sách có tồn tại không
            book_info = next((b for b in books if b['id'] == book_id), None)
            
            if not book_info:
                return JsonResponse({'error': 'Sach khong ton tai ben Book Service'}, status=404)
            
            price = book_info['price']
            
        except Exception as e:
            return JsonResponse({'error': 'Khong lien lac duoc voi Book Service: ' + str(e)}, status=500)

        # BƯỚC 2: LƯU VÀO DATABASE CỦA CART SERVICE
        cart, _ = Cart.objects.get_or_create(customer_id=customer_id)
        CartItem.objects.create(
            cart=cart,
            book_id=book_id,
            quantity=quantity,
            price=price # Lưu giá lấy được từ Book Service
        )

        return JsonResponse({'message': 'Them vao gio thanh cong', 'price': price})
        
    return JsonResponse({'error': 'Sai method'}, status=405)