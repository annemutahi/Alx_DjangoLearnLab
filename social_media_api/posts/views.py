from rest_framework import viewsets, permissions, filters, status, generics
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from notifications.utils import create_notification
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

User = get_user_model()

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # allow ?search=keyword

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You can only edit your own posts.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own posts.")
        instance.delete()



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You can only edit your own comments.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own comments.")
        instance.delete()

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # Get users that the current user follows
        following_users = user.following.all()
        # Filter posts by those authors
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
    
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        # Prevent duplicate likes
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create like
        Like.objects.create(user=request.user, post=post)

        # Create notification (avoid self-notifications)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
@login_required
def like_post(request, pk):
    # Use DRF's get_object_or_404 for safety and clarity
    post = generics.get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        # The user already liked the post
        return JsonResponse({'error': 'You have already liked this post.'}, status=400)

    # Trigger a notification for the post author
    create_notification(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target=post
    )

    return JsonResponse({'message': 'Post liked successfully.'}, status=200)


@login_required
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)

    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return JsonResponse({'message': 'Post unliked successfully.'}, status=200)
    except Like.DoesNotExist:
        return JsonResponse({'error': 'You have not liked this post.'}, status=400)