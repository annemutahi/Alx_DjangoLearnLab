from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        # Login with the test user
        self.client.login(username="testuser", password="password123")
        # Create a sample book
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )

    def test_book_list_authenticated(self):
        url = reverse("book-list")  # Adjust name if needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("1984", str(response.data))

    def test_create_book_authenticated(self):
        url = reverse("book-list")
        data = {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
