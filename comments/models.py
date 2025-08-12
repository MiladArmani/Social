from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Comment(models.Model):
    """
    Represents a comment made by a user on a post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post: Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content: models.TextField = models.TextField()
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on {self.post.title}"
