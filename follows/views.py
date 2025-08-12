from rest_framework import generics, permissions
from typing import Any
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer


class FollowListCreateView(generics.ListCreateAPIView):
    """
    API view to list all follow relationships of the current authenticated user
    and to create a new follow relationship.

    Methods:
        - GET: Retrieve all users the current user is following.
        - POST: Follow a new user by their ID.
    """

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> Any:
        """
        Return a list of Follow objects where the current user is the follower.

        Returns:
            QuerySet: A queryset containing the follow relationships of the user.
        """
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer: FollowSerializer) -> None:
        """
        Save a new follow relationship with the current user as the follower.

        Args:
            serializer (FollowSerializer): The validated serializer instance.
        """
        serializer.save(follower=self.request.user)


class FollowCreateView(generics.CreateAPIView):
    """
    API endpoint to follow a user.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: FollowSerializer) -> None:
        """
        Save the follow with the current authenticated user as follower.
        """
        serializer.save(follower=self.request.user)


class FollowersListView(generics.ListAPIView):
    """
    API endpoint to list all followers of a specific user.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self) -> Any:
        """
        Retrieve all followers for the given user ID.

        Returns:
            QuerySet: Followers for a given user.
        """
        user_id: int = self.kwargs["user_id"]
        return Follow.objects.filter(following_id=user_id)


class FollowingListView(generics.ListAPIView):
    """
    API endpoint to list all users a specific user is following.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self) -> Any:
        """
        Retrieve all following users for the given user ID.

        Returns:
            QuerySet: Followed users for a given user.
        """
        user_id: int = self.kwargs["user_id"]
        return Follow.objects.filter(follower_id=user_id)


class UnfollowView(generics.DestroyAPIView):
    """
    API endpoint to unfollow a user.
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Follow:
        """
        Retrieve the follow instance for the authenticated user.

        Returns:
            Follow: The follow object.
        """
        user_id: int = self.kwargs["user_id"]
        return Follow.objects.get(follower=self.request.user, following_id=user_id)
