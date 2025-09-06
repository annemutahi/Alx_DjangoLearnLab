from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail')
]