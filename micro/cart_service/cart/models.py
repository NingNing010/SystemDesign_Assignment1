from django.db import models

class Cart(models.Model):
    # Chỉ lưu ID khách hàng (dạng số), không quan hệ bảng
    customer_id = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # Chỉ lưu ID sách (dạng số)
    book_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    
    # Lưu giá tại thời điểm mua (đề phòng bên Book Service đổi giá)
    price = models.DecimalField(max_digits=10, decimal_places=2)