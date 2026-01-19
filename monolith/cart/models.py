from django.db import models
from django.conf import settings
from books.models import Book

class Cart(models.Model):
    # Đề bài: id, customer_id, created_at [cite: 241]
    # Liên kết 1-1 với Customer (Mỗi người 1 giỏ)
    customer = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart của {self.customer.username}"

class CartItem(models.Model):
    # Đề bài: id, cart_id, book_id, quantity [cite: 241]
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"