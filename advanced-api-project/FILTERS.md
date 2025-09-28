API Filtering, Searching & Ordering

The BookListView supports advanced query features:

Filtering – filter by title, author, or publication_year

GET /api/books/?author=George Orwell
GET /api/books/?publication_year=1949


Searching – full-text search on title and author

GET /api/books/?search=1984


Ordering – sort results by any field (default: ascending; prefix with - for descending)

GET /api/books/?ordering=title
GET /api/books/?ordering=-publication_year

Requirements

django-filter must be installed and added to INSTALLED_APPS.

Ensure DEFAULT_FILTER_BACKENDS in settings.py includes:

'django_filters.rest_framework.DjangoFilterBackend',
'rest_framework.filters.SearchFilter',
'rest_framework.filters.OrderingFilter',