from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user and authenticate client
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.client = APIClient()
        self.auth_client = APIClient()
        self.auth_client.login(username="testuser", password="pass1234")

        # Sample book
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

    # -------- CRUD TESTS --------
    def test_create_book_authenticated(self):
        data = {"title": "Brave New World", "author": "Aldous Huxley", "publication_year": 1932}
        response = self.auth_client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Fahrenheit 451", "author": "Ray Bradbury", "publication_year": 1953}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_update_book_authenticated(self):
        data = {"title": "Nineteen Eighty-Four", "author": "George Orwell", "publication_year": 1949}
        response = self.auth_client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_update_book_unauthenticated(self):
        data = {"title": "Nineteen Eighty-Four"}
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        response = self.auth_client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # -------- FILTERING / SEARCH / ORDERING --------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=George Orwell")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + "?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_order_books_by_year_desc(self):
        Book.objects.create(title="Animal Farm", author="George Orwell", publication_year=1945)
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))