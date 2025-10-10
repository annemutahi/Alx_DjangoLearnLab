from django.urls import path
from .views import RegisterView, LoginView, ProfileView, UserViewSet

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'),
]