The comment system allows authenticated users to interact with blog posts by leaving comments. Each comment is tied to a specific blog post and authored by a registered user. Users can create, edit, and delete their own comments, while post owners and admins may moderate them if necessary.

Features
1. Add Comments

Requirement: User must be authenticated (logged in).

Steps:

Navigate to the detail page of a blog post.

Scroll down to the comment section.

Fill out the comment form with your text.

Submit the form to post your comment.

Result: The comment is saved to the database, linked to the post and user, and displayed immediately below the post.

2. Edit Comments

Requirement: User must be the author of the comment.

Steps:

Locate your comment under the blog post.

Click the Edit option.

Update your comment in the form.

Submit to save changes.

Result: The updated_at timestamp is modified, and the new content is displayed.

3. Delete Comments

Requirement: User must be the author of the comment (or an admin).

Steps:

Locate your comment under the blog post.

Click the Delete option.

Confirm the deletion action.

Result: The comment is permanently removed from the database.

Permissions and Rules

Visibility:

All users (authenticated or not) can view comments on a post.

Creation:

Only logged-in users can add new comments.

Editing/Deleting:

Only the comment author can edit or delete their comment.

Admin users may also delete inappropriate comments.

Timestamps:

created_at: When the comment was originally posted.

updated_at: Last time the comment was edited.