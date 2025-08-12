from rest_framework import serializers
from typing import Any
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    
    Converts Like instances to JSON and validates incoming data for creating likes.
    """

    user_username = serializers.CharField(source="user.username", read_only=True)
    post_title = serializers.CharField(source="post.title", read_only=True)

    class Meta:
        model = Like
        fields: tuple[str, ...] = ("id", "user", "user_username", "post", "post_title", "created_at")
        read_only_fields: tuple[str, ...] = ("id", "created_at")

    def create(self, validated_data: dict[str, Any]) -> Like:
        """
        Create a new Like instance.

        Args:
            validated_data (dict[str, Any]): The validated data for the like.

        Returns:
            Like: The newly created Like object.
        """
        return Like.objects.create(**validated_data)
