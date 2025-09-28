Testing Guide – Book API
Testing Strategy

Use Django’s built-in test framework (unittest) with DRF’s APIClient.

Tests run against a temporary test database (safe – won’t touch dev/prod DB).

Covers:

CRUD operations

Filtering, searching, and ordering

Permissions & authentication

Test Cases Covered

CRUD Tests

Create Book → 201 Created with saved data.

Retrieve Book(s) → 200 OK with correct details.

Update Book → Authenticated only; unauthenticated gets 403 Forbidden.

Delete Book → Authenticated only; unauthenticated gets 403 Forbidden.

Filter/Search/Ordering Tests

/api/books/?author=George Orwell → only Orwell’s books.

/api/books/?search=1984 → matches title.

/api/books/?ordering=-publication_year → sorted results.

Permission Tests

Authenticated users can create, update, delete.

Unauthenticated users get read-only access.

Running the Tests

Run inside project root:

python manage.py test api

Interpreting Results
Example: All Tests Pass
Found 11 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 2.345s

OK

Example: Test Failure
FAIL: test_create_book_unauthenticated (api.tests.BookAPITests)
----------------------------------------------------------------------
Traceback (most recent call last):
  AssertionError: 403 != 201

----------------------------------------------------------------------
Ran 11 tests in 2.210s

FAILED (failures=1)


403 != 201 → The API returned Forbidden when test expected Created.

Use the traceback to locate and fix the bug.