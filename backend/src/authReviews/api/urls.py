from django.urls import path

from .views import (
    AuthorReviewCreateView,
    AuthorReviewListView,
    AuthorReviewLikeView,
    AuthorReviewUserListView
)

urlpatterns = [
    path('<fk>', AuthorReviewListView.as_view(), name="authreviewlist"),
    path('create/', AuthorReviewCreateView.as_view(), name='authcreatereview'),
    path('like/<pk>', AuthorReviewLikeView.as_view(), name='authlikereview'),
    path('user/<fk>', AuthorReviewUserListView.as_view(), name="authuserreviewlist")
    
]