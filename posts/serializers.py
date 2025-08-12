# posts/serializers.py
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and retrieving Post objects.
    """
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'content', 'image', 'created_at', 'updated_at')
        read_only_fields = ('author', 'created_at', 'updated_at')
