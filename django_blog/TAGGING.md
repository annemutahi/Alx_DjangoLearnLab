Tagging & Search Features
1. Adding Tags to Posts

When creating or editing a post, you will see a Tags field in the form.

Enter one or more tags separated by commas (e.g., django, python, web).

New tags that don’t exist yet will be automatically created in the database.

Tags help group related posts together, making content easier to discover.

Example:
Title: "Getting Started with Django"
Content: "Django is a Python framework..."
Tags: django, python, backend


This post will now be accessible under the Django and Python tag pages.

2. Viewing Posts by Tag

On each post’s detail page, tags are displayed at the bottom.

Tags are clickable links. Clicking a tag (e.g., django) will take you to /tags/django/, which lists all posts associated with that tag.

Example URL:
/tags/python/


Shows all posts tagged with python.

3. Searching Posts

A search bar is available at the top of the blog or on the search page.

Users can enter keywords to find posts by:

Title

Content

Tags

Example Search:
/search/?q=django


This will return all posts that:

Have “django” in the title,

Contain “django” in the content, or

Are tagged with “django”.

4. Combining Tagging and Search

Tags narrow content by category, while search allows free-text exploration.

Users can browse by tags for structured exploration, or search to quickly find specific content.

5. Permissions & Data Handling Notes

Only authenticated users with post creation/edit permissions can add or edit tags.

Tags are shared globally — multiple posts can reuse the same tag.

Search queries are read-only: no personal data is exposed, and search results only display content that is already public.