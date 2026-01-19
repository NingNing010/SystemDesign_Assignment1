# infrastructure/repositories.py
from domain.entities import Book, Cart, CartItem
from usecases.managers import BookRepositoryInterface, CartRepositoryInterface
from .models import BookORM, CartORM, CartItemORM

# 1. Repository quản lý sách
class DjangoBookRepository(BookRepositoryInterface):
    def get_all_books(self):
        # Lấy dữ liệu từ Django ORM
        orm_books = BookORM.objects.all()
        # Chuyển đổi sang Domain Entity (để Use Case hiểu được)
        return [
            Book(id=b.id, title=b.title, author=b.author, price=b.price, stock=b.stock)
            for b in orm_books
        ]

# 2. Repository quản lý giỏ hàng
class DjangoCartRepository(CartRepositoryInterface):
    def get_cart_by_user(self, user_id: int):
        try:
            orm_cart = CartORM.objects.get(user_id=user_id)
            # Convert items
            items = []
            for item in orm_cart.items.all():
                domain_book = Book(
                    id=item.book.id, title=item.book.title, 
                    author=item.book.author, price=item.book.price, stock=item.book.stock
                )
                items.append(CartItem(book=domain_book, quantity=item.quantity))
            
            return Cart(id=orm_cart.id, customer_id=orm_cart.user_id, items=items, created_at=orm_cart.created_at)
        except CartORM.DoesNotExist:
            return None

    def create_cart(self, user_id: int):
        orm_cart = CartORM.objects.create(user_id=user_id)
        return Cart(id=orm_cart.id, customer_id=orm_cart.user_id, items=[], created_at=orm_cart.created_at)

    def add_item(self, cart_id: int, book: Book, quantity: int):
        # Lưu vào Database thông qua Django Models
        cart_orm = CartORM.objects.get(id=cart_id)
        book_orm = BookORM.objects.get(id=book.id)
        
        item, created = CartItemORM.objects.get_or_create(cart=cart_orm, book=book_orm)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()