from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('is_read', '-timestamp')

    data = [
        {
            'id': n.id,
            'actor': str(n.actor),
            'verb': n.verb,
            'target': str(n.target) if n.target else None,
            'timestamp': n.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'is_read': n.is_read
        }
        for n in notifications
    ]
    return JsonResponse({'notifications': data})


@login_required
def mark_notification_as_read(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'message': 'Notification marked as read.'})
    except Notification.DoesNotExist:
        return JsonResponse({'error': 'Notification not found.'}, status=404)