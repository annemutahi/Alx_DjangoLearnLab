A Django REST Framework (DRF)-based API providing user registration, authentication, and profile management for a social media application.


Register a new user. Endpoint:
POST /api/register/

Request body (JSON):

{
  "username": "princess",
  "email": "princess@example.com",
  "password": "securePass123"
}


Response:

{
  "id": 1,
  "username": "princess",
  "email": "princess@example.com",
  "bio": "",
  "profile_picture": null
}

🔹 Login and retrieve token

Endpoint:
POST /api/token-auth/

Request body (JSON):

{
  "username": "princess",
  "password": "securePass123"
}


Response:

{
  "token": "5a69b7f96e4e18e53c5f1..."
}

🔹 Authenticated requests

Include your token in the request header:

Authorization: Token your_token_here


Example (curl):

curl -H "Authorization: Token 5a69b7f96e4e18e53c5f1..." \
     http://127.0.0.1:8000/api/profile/


All authentication uses DRF TokenAuthentication.

The Browsable API can be tested at http://127.0.0.1:8000/api/register/