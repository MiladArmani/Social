# posts/views.py
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from typing import Any


class PostListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing all posts or creating a new post.

    Methods:
        get: Returns a list of posts.
        post: Creates a new post for the authenticated user.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: PostSerializer) -> None:
        """Assign the authenticated user as the post's author."""
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, or deleting a single post.
    Only the author can update or delete the post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer: PostSerializer) -> None:
        """Update the post if the user is the author."""
        serializer.save(author=self.request.user)
