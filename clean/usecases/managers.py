# usecases/managers.py
from typing import List
from domain.entities import Book, Cart, CartItem

# Định nghĩa Interface (Hợp đồng) cho kho chứa dữ liệu
# Use Case không cần biết Database là MySQL hay file text, nó chỉ cần biết có cái kho này.
class BookRepositoryInterface:
    def get_all_books(self) -> List[Book]:
        pass

class CartRepositoryInterface:
    def get_cart_by_user(self, user_id: int) -> Cart:
        pass
    def add_item(self, cart_id: int, book: Book, quantity: int):
        pass
    def create_cart(self, user_id: int) -> Cart:
        pass

# --- Logic Nghiệp vụ ---

class ListBooksUseCase:
    def __init__(self, repo: BookRepositoryInterface):
        self.repo = repo

    def execute(self) -> List[Book]:
        return self.repo.get_all_books()

class AddToCartUseCase:
    def __init__(self, cart_repo: CartRepositoryInterface, book_repo: BookRepositoryInterface):
        self.cart_repo = cart_repo
        self.book_repo = book_repo

    def execute(self, user_id: int, book_id: int, quantity: int):
        # 1. Lấy giỏ hàng (nếu chưa có thì tạo mới)
        cart = self.cart_repo.get_cart_by_user(user_id)
        if not cart:
            cart = self.cart_repo.create_cart(user_id)
        
        # 2. Lấy thông tin sách (để đảm bảo sách tồn tại)
        books = self.book_repo.get_all_books()
        book = next((b for b in books if b.id == book_id), None)
        
        if not book:
            raise Exception("Book not found")
        
        # 3. Thêm vào giỏ
        self.cart_repo.add_item(cart.id, book, quantity)
        return cart.id