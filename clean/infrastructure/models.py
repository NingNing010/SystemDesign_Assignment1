# infrastructure/models.py
from django.db import models

class BookORM(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'books' # Đặt tên bảng trong MySQL

class CartORM(models.Model):
    # Dùng user_id dạng số thay vì quan hệ ForeignKey phức tạp để đơn giản hóa Clean Arch
    user_id = models.IntegerField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'carts'

class CartItemORM(models.Model):
    cart = models.ForeignKey(CartORM, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(BookORM, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    class Meta:
        db_table = 'cart_items'