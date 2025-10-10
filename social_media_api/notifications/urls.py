from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_notifications, name='user-notifications'),
    path('<int:notification_id>/read/', views.mark_notification_as_read, name='mark-as-read'),
]