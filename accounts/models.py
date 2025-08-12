from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    User profile model for storing additional user information.

    Attributes:
        user (User): One-to-one link to the default Django User model.
        bio (str): Short biography of the user.
        avatar (ImageField): Profile picture of the user.
        location (str): Geographic location of the user.
    """
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    bio: str = models.TextField(blank=True)
    avatar: models.ImageField = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location: str = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        """
        Return the username of the associated user.
        """
        return self.user.username
