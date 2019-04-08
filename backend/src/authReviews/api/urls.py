from django.urls import path

from .views import (
    AuthorReviewCreateView,
    AuthorReviewListView,
    AuthorReviewLikeView,
    AuthorReviewUserListView
)

urlpatterns = [
    path('<fk>', AuthorReviewListView.as_view(), name="reviewlist"),
    path('create/', AuthorReviewCreateView.as_view(), name='createreview'),
    path('like/<pk>', AuthorReviewLikeView.as_view(), name='likereview'),
    path('user/<fk>', AuthorReviewUserListView.as_view(), name="userreviewlist")
    
]