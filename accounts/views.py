# accounts/views.py
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from typing import Any


class RegisterView(generics.CreateAPIView):
    """
    API endpoint for registering new users.

    Methods:
        post: Create a new user account.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile_view(request) -> Response:
    """
    Retrieve the authenticated user's profile information.

    Args:
        request: HTTP request object.

    Returns:
        Response: Serialized user data.
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
