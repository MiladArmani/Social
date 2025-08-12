# posts/models.py
from django.db import models
from django.contrib.auth.models import User
from typing import Any


class Post(models.Model):
    """
    Represents a user's post in the social media app.

    Attributes:
        author (User): The user who created the post.
        content (str): The main text content of the post.
        image (ImageField): Optional image for the post.
        created_at (datetime): The date and time when the post was created.
        updated_at (datetime): The date and time when the post was last updated.
    """
    author: User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content: str = models.TextField()
    image: Any = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Return a string representation of the post."""
        return f"Post by {self.author.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
