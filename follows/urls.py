from django.urls import path
from .views import (
    FollowListCreateView,
    FollowCreateView,
    FollowersListView,
    FollowingListView,
    UnfollowView,
)

urlpatterns = [
    path("", FollowListCreateView.as_view(), name="follows-list-create"),  
    path("follow/<int:user_id>/", FollowCreateView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowView.as_view(), name="unfollow-user"),
    path("followers/<int:user_id>/", FollowersListView.as_view(), name="followers-list"),
    path("following/<int:user_id>/", FollowingListView.as_view(), name="following-list"),
]
