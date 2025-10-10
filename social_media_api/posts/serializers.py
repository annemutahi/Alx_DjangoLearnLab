from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import RegisterSerializer
from accounts.models import User
from django.contrib.auth import get_user_model

class CommentSerializer(serializers.ModelSerializer):
    author = RegisterSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']    

class PostSerializer(serializers.ModelSerializer):
    author = RegisterSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']