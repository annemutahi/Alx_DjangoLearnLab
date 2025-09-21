from django.contrib import admin
from django.urls import path
from .views import book_list
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('books/', book_list, name='book-list'),
]