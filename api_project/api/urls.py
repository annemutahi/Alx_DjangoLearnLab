from django.contrib import admin
from django.urls import path
from .views import book_list, BookList
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books/', book_list, name='booklist'),
    path('books/', BookList.as_view(), name='book-list'),
]