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
    path('relationship_app/admin_view.html/', views.admin_view, name='admin_dashboard'),
    path('relationship_app/librarian_view.html/', views.librarian_view, name='librarian_dashboard'),
    path('relationship_app/member_view.html/', views.member_view, name='member_dashboard'),
]
