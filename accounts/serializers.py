# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles user creation with password validation.
    """
    password: serializers.CharField = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2: serializers.CharField = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'email': {'required': True}}

    def validate(self, attrs: dict) -> dict:
        """Ensure password fields match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data: dict) -> User:
        """Create and return a new user instance."""
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving user profile details.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
