from django.contrib import admin
from django.urls import path
from .views import BookListView, LibrarydetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView, name='book-list'),
    path('library/<int:pk>/', LibrarydetailView.as_view(), name ='library-detail')
]
