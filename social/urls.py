# social/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from typing import Any


def home(request) -> Any:
    """Root endpoint for API status check."""
    return JsonResponse({"message": "Welcome to the Social Media API"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/accounts/', include('accounts.urls')),
    path('api/posts/', include('posts.urls')),
    path("api/follows/", include("follows.urls")),
    path("api/likes/", include("likes.urls")),
    path("api/comments/", include("comments.urls")),
]
