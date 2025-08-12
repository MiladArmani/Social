from rest_framework import generics, permissions
from typing import Any
from .models import Comment
from .serializers import CommentSerializer


class CommentCreateView(generics.CreateAPIView):
    """
    API endpoint to create a comment for a post.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: CommentSerializer) -> None:
        """
        Save the comment with the current authenticated user.
        """
        serializer.save(user=self.request.user)


class CommentListView(generics.ListAPIView):
    """
    API endpoint to list all comments for a specific post.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self) -> Any:
        """
        Retrieve all comments for the given post ID.

        Returns:
            QuerySet: Comments for the post.
        """
        post_id: int = self.kwargs["post_id"]
        return Comment.objects.filter(post_id=post_id)


class CommentDeleteView(generics.DestroyAPIView):
    """
    API endpoint to delete a comment.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> Comment:
        """
        Retrieve the comment belonging to the authenticated user.

        Returns:
            Comment: The comment object.
        """
        comment_id: int = self.kwargs["comment_id"]
        return Comment.objects.get(id=comment_id, user=self.request.user)
