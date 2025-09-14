from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_dashboard'),
    path('librarian_view/', views.librarian_view, name='librarian_dashboard'),
    path('member_view/', views.member_view, name='member_dashboard'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
