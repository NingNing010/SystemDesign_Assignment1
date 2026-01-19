# interfaces/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Import các lớp từ vòng tròn bên trong
from infrastructure.repositories import DjangoBookRepository, DjangoCartRepository
from usecases.managers import ListBooksUseCase, AddToCartUseCase

def list_books_api(request):
    # 1. Khởi tạo các thành phần (Dependency Injection)
    repo = DjangoBookRepository()
    use_case = ListBooksUseCase(repo)
    
    # 2. Thực thi Use Case
    books = use_case.execute()
    
    # 3. Chuyển đổi kết quả Entity sang JSON để trả về
    data = [
        {"id": b.id, "title": b.title, "author": b.author, "price": b.price, "stock": b.stock}
        for b in books
    ]
    return JsonResponse({"books": data})

@csrf_exempt
def add_to_cart_api(request):
    if request.method == 'POST':
        try:
            # 1. Lấy dữ liệu từ request
            body = json.loads(request.body)
            book_id = body.get('book_id')
            quantity = body.get('quantity', 1)
            user_id = 123  # Giả định user ID cố định vì chưa làm login
            
            # 2. Khởi tạo (Lắp ghép)
            cart_repo = DjangoCartRepository()
            book_repo = DjangoBookRepository()
            use_case = AddToCartUseCase(cart_repo, book_repo)
            
            # 3. Thực thi Use Case
            cart_id = use_case.execute(user_id, book_id, quantity)
            
            return JsonResponse({"message": "Success", "cart_id": cart_id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
            
    return JsonResponse({"error": "Method not allowed"}, status=405)