from rest_framework import serializers
from typing import Any
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    
    Converts Comment instances to JSON and validates incoming data for creating comments.
    """

    user_username = serializers.CharField(source="user.username", read_only=True)
    post_title = serializers.CharField(source="post.title", read_only=True)

    class Meta:
        model = Comment
        fields: tuple[str, ...] = ("id", "user", "user_username", "post", "post_title", "content", "created_at")
        read_only_fields: tuple[str, ...] = ("id", "created_at")

    def create(self, validated_data: dict[str, Any]) -> Comment:
        """
        Create a new Comment instance.

        Args:
            validated_data (dict[str, Any]): The validated data for the comment.

        Returns:
            Comment: The newly created Comment object.
        """
        return Comment.objects.create(**validated_data)
