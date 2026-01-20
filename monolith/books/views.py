from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    # Render ra giao diện HTML thay vì JsonResponse
    return render(request, 'books/book_list.html', {'books': books})