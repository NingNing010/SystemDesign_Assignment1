from django.http import JsonResponse
from .models import Book

def get_books(request):
    books = Book.objects.all()
    data = list(books.values('id', 'title', 'author', 'price', 'stock'))
    return JsonResponse({'books': data})