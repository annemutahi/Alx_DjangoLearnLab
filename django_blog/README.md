This is a simple blog web application built with Django. It supports full CRUD operations (Create, Read, Update, Delete) for blog posts and enforces user permissions to ensure content security.

 Features
Post Listing (Home Page)

Displays all published blog posts in reverse chronological order.

Shows each post’s title, author, and a snippet of content.

Links to individual post detail pages.

Template: post_list.html

Post Detail View

Shows the full content of a blog post.

Displays author name and published date.

Provides Edit and Delete buttons only for the post’s author.

Template: post_detail.html

Create Post

Logged-in users can create new posts.

A form (PostForm) is provided for entering title and content.

The post’s author is automatically set to the currently logged-in user (not selectable in the form).

Template: post_form.html

Edit Post

Only the author of a post can edit it.

Uses the same form as creation (PostForm).

Permission enforced via UserPassesTestMixin in the view.

Template: post_form.html

Delete Post

Only the author can delete their own post.

Requires confirmation before deletion.

Redirects back to the post list after deletion.

Template: post_confirm_delete.html

Authentication

Blog integrates with Django’s built-in authentication system.

Unauthenticated users can only view posts.

Authenticated users can create, edit, and delete their own posts.

Permissions & Data Handling

Post Ownership: Only the user who created a post can update or delete it.

Author Field: Automatically assigned when a post is created. Users cannot modify it.

Data Security: Forms are CSRF-protected by Django by default.

Validation: Title and content are required fields; empty submissions are rejected.

Testing

Unit tests (tests.py) cover:

Creating posts (only for logged-in users).

Updating/deleting posts (restricted to author only).

Viewing post lists and details (available to all).

Navigation between pages and correct template rendering.

Run tests with:

python manage.py test

Templates Overview

post_list.html → List all posts.

post_detail.html → Show full post.

post_form.html → Used for both create and edit forms.

post_confirm_delete.html → Confirm deletion of a post.