from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostViewTests(TestCase):
    def setUp(self):
        # create two users
        self.user1 = User.objects.create_user(username="user1", password="pass1234")
        self.user2 = User.objects.create_user(username="user2", password="pass1234")
        # create a post by user1
        self.post = Post.objects.create(title="Test Post", content="Content here", author=self.user1)

    def test_post_list_view(self):
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post-detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Content here")

    def test_create_view_authenticated(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.post(reverse("post-create"), {
            "title": "New Post", "content": "New content"
        })
        self.assertEqual(Post.objects.count(), 2)  # new post created

    def test_create_view_unauthenticated_redirects(self):
        response = self.client.get(reverse("post-create"))
        self.assertNotEqual(response.status_code, 200)  # should redirect to login

    def test_update_view_author_only(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.post(reverse("post-update", args=[self.post.pk]), {
            "title": "Updated Title", "content": "Updated body"
        })
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Title")

    def test_update_view_other_user_forbidden(self):
        self.client.login(username="user2", password="pass1234")
        response = self.client.get(reverse("post-update", args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)

    def test_delete_view_author_only(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.post(reverse("post-delete", args=[self.post.pk]))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_delete_view_other_user_forbidden(self):
        self.client.login(username="user2", password="pass1234")
        response = self.client.get(reverse("post-delete", args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)

