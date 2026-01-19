from django.db import models

class Book(models.Model):
    # Đề bài yêu cầu: id, title, author, price, stock [cite: 241]
    # (Trường 'id' Django tự tạo, không cần viết)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Giá tiền
    stock = models.IntegerField(default=0) # Số lượng tồn kho

    def __str__(self):
        return self.title