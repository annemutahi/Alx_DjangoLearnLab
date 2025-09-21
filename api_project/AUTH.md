Authentication

This API uses Django REST Framework’s Token Authentication.

Each user has a unique token that must be sent with requests.

Tokens are issued by sending a POST request with a username and password.

How to obtain a token

Send a POST request to /api-token-auth/ with your credentials:

curl -X POST http://127.0.0.1:8000/api-token-auth/ \
     -d "username=admin&password=yourpassword"


Response:

{"token": "abc123def456..."}

📡 Using your token

Once you have a token, include it in the Authorization header for all API requests:

Authorization: Token abc123def456...


Example request:

curl -H "Authorization: Token abc123def456..." \
     http://127.0.0.1:8000/books_all/

Permissions

Permissions control who can access what in the API.

IsAuthenticated (default): Only logged-in users with a valid token or session can access.

IsAdminUser (optional): Only admin/staff accounts can access.

Custom permissions: Can be added (e.g., only the user who made a reservation can edit/cancel it).

Current configuration:

BookList and BookViewSet are protected with IsAuthenticated.
This means you must be logged in (with a token) to view or modify books.