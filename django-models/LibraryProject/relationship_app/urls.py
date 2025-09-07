from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name ='library-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
]