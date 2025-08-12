from django.db import models
from django.utils import timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.contrib.auth.models import User
    from posts.models import Post


class Like(models.Model):
    """
    Represents a like given by a user to a specific post.

    Attributes:
        user (User): The user who liked the post.
        post (Post): The post that received the like.
        created_at (datetime): The date and time when the like was created.
    """

    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="likes"
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        Returns a string representation of the like.

        Returns:
            str: A string showing which user liked which post.
        """
        return f"{self.user.username} liked '{self.post.title}'"
