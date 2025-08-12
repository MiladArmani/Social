from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from typing import Any
from .models import Like
from .serializers import LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new like for a post.

    Only authenticated users can like a post.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: LikeSerializer) -> None:
        """
        Save the like with the current authenticated user.

        Args:
            serializer (LikeSerializer): The serializer instance.
        """
        serializer.save(user=self.request.user)


class LikeListView(generics.ListAPIView):
    """
    API endpoint to list all likes for a specific post.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self) -> Any:
        """
        Retrieve likes filtered by a given post ID from URL parameters.

        Returns:
            QuerySet: List of likes for the given post.
        """
        post_id: int = self.kwargs["post_id"]
        return Like.objects.filter(post_id=post_id)


class LikeDeleteView(generics.DestroyAPIView):
    """
    API endpoint to remove a like from a post.

    Only the user who liked the post can unlike it.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Like:
        """
        Retrieve the like object belonging to the authenticated user for a given post.

        Returns:
            Like: The like instance.
        """
        post_id: int = self.kwargs["post_id"]
        return Like.objects.get(user=self.request.user, post_id=post_id)
