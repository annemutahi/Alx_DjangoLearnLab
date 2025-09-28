Book API

Overview

This API provides CRUD operations for the Book model using Django REST Framework generic views.

Endpoints

ListView (/api/books/) – Retrieve all books (read-only for unauthenticated users).

DetailView (/api/books/<id>/) – Retrieve a single book by ID (read-only for unauthenticated users).

CreateView (/api/books/create/) – Add a new book (authenticated users only).

UpdateView (/api/books/<id>/update/) – Modify an existing book (authenticated users only).

DeleteView (/api/books/<id>/delete/) – Remove a book (authenticated users only).

Permissions

Read-only access: unauthenticated users (List & Detail).

Write access: authenticated users (Create, Update, Delete).

Authentication

Token authentication enabled via rest_framework.authtoken.

Obtain token:

python manage.py drf_create_token <username>

Use token in requests:
curl -H "Authorization: Token <your_token>" http://localhost:8000/api/books/

