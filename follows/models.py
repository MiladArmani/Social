from django.db import models
from django.utils import timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.contrib.auth.models import User


class Follow(models.Model):
    """
    Represents a follow relationship between two users.

    Attributes:
        follower (User): The user who follows another user.
        following (User): The user who is being followed.
        created_at (datetime): The date and time when the follow action was created.
    """

    follower = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="following"
    )
    following = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="followers"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        """
        Returns a string representation of the follow relationship.

        Returns:
            str: A string showing who follows who.
        """
        return f"{self.follower.username} follows {self.following.username}"
