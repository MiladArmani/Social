from rest_framework import serializers
from typing import Any
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follow model.
    
    Converts Follow instances to JSON and validates incoming data for creating follows.
    """

    follower_username = serializers.CharField(source="follower.username", read_only=True)
    following_username = serializers.CharField(source="following.username", read_only=True)

    class Meta:
        model = Follow
        fields: tuple[str, ...] = ("id", "follower", "follower_username", "following", "following_username", "created_at")
        read_only_fields: tuple[str, ...] = ("id", "created_at")

    def create(self, validated_data: dict[str, Any]) -> Follow:
        """
        Create a new Follow instance.

        Args:
            validated_data (dict[str, Any]): The validated data for the follow.

        Returns:
            Follow: The newly created Follow object.
        """
        return Follow.objects.create(**validated_data)
