from django.shortcuts import render
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer

def book_list(request):
    books = Book.objects.all()
    return render(request, 'api/book_list.html', {'books': books})

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

