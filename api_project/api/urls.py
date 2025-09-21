from django.contrib import admin
from django.urls import path,include
from .views import book_list, BookList, BookViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books/', book_list, name='booklist'),
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]