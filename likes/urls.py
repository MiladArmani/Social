from django.urls import path
from .views import LikeCreateView, LikeListView, LikeDeleteView

urlpatterns = [
    path("post/<int:post_id>/likes/", LikeListView.as_view(), name="like-list"),
    path("post/<int:post_id>/like/", LikeCreateView.as_view(), name="like-create"),
    path("post/<int:post_id>/unlike/", LikeDeleteView.as_view(), name="like-delete"),
]
