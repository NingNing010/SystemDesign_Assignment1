from django.db import models
from django.conf import settings  # Để lấy User model chuẩn

# 1. XÓA dòng này đi:
# from books.models import Book  <-- XÓA DÒNG NÀY
# from accounts.models import Customer <-- XÓA DÒNG NÀY (nếu có)

class Cart(models.Model):
    # Dùng settings.AUTH_USER_MODEL thay vì import Customer trực tiếp
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    
    # 2. Sửa dòng này: Dùng chuỗi 'books.Book' thay vì biến Book
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE) 
    
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"