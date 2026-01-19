# domain/entities.py
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

# --- Pure Python Classes (Không dính dáng gì đến Django Models) ---

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    price: float
    stock: int

@dataclass
class Customer:
    id: Optional[int]
    name: str
    email: str

@dataclass
class CartItem:
    book: Book
    quantity: int

    @property
    def total_price(self):
        return self.book.price * self.quantity

@dataclass
class Cart:
    id: Optional[int]
    customer_id: int
    items: List[CartItem]
    created_at: datetime