"""
Django Permissions & Groups Setup Guide
---------------------------------------

1. Custom Permissions:
   - In `models.py`, we defined extra permissions on our model (e.g. Book):
       can_view   → Allows viewing instances of the model
       can_create → Allows creating new instances
       can_edit   → Allows editing existing instances
       can_delete → Allows deleting instances

   Example (inside Book model):
   class Meta:
       permissions = [
           ("can_view", "Can view book"),
           ("can_create", "Can create book"),
           ("can_edit", "Can edit book"),
           ("can_delete", "Can delete book"),
       ]

2. Groups:
   - Groups are roles that hold permissions. Users inherit permissions through groups.
   - We created these groups:
       Editors → has can_edit, can_create
       Viewers → has can_view
       Admins  → has can_view, can_create, can_edit, can_delete

3. Users:
   - Users are assigned to groups. For example:
       alice → Editors
       bob   → Viewers
       carol → Admins

4. Enforcing Permissions in Views:
   - Use the @permission_required decorator in views to restrict access:
       @permission_required("bookshelf.can_edit", raise_exception=True)
       def edit_book(request, pk): ...
   - This ensures only users (or groups) with that permission can access the view.

5. Manual Testing:
   - Log in as different users and try accessing create/edit/delete pages.
   - Expected:
       Viewers → can only view
       Editors → can create & edit but not delete
       Admins  → full access
"""

from bookshelf.models import CustomUser
from django.contrib.auth.models import Group

# Create users with email addresses
alice = CustomUser.objects.create_user(
    username="alice",
    email="alice@example.com",
    password="pass123"
)

bob = CustomUser.objects.create_user(
    username="bob",
    email="bob@example.com",
    password="pass123"
)

carol = CustomUser.objects.create_user(
    username="carol",
    email="carol@example.com",
    password="pass123"
)

# Fetch groups (assumes they were created in admin or migrations)
editors = Group.objects.get(name="Editors")
viewers = Group.objects.get(name="Viewers")
admins = Group.objects.get(name="Admins")

# Assign users to groups
alice.groups.add(editors)
bob.groups.add(viewers)
carol.groups.add(admins)
