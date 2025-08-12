from django.urls import path
from .views import CommentCreateView, CommentListView, CommentDeleteView

urlpatterns = [
    path("post/<int:post_id>/comments/", CommentListView.as_view(), name="comment-list"),
    path("post/<int:post_id>/comment/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:comment_id>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
