from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]   # author excluded for security

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if len(body) < 10:
            raise forms.ValidationError("Content must be at least 10 characters long.")
        return body