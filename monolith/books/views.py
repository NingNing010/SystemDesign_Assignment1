from django.http import JsonResponse
from .models import Book

def book_list(request):
    # Lấy tất cả sách từ database
    books = Book.objects.all()
    
    # Chuyển đổi dữ liệu thành dạng danh sách (JSON)
    data = list(books.values('id', 'title', 'author', 'price', 'stock'))
    
    # Trả về kết quả JSON
    return JsonResponse({'books': data})