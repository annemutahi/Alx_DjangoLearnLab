from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
from rest_framework import status

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )

    def test_book_list_authenticated(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_create_book_authenticated(self):
        url = reverse("book-list")
        data = {"title": "Animal Farm", "author": "George Orwell", "publication_year": 1945}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
