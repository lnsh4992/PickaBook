from django.urls import path

from .views import (
    BookReviewCreateView,
    BookReviewListView,
    BookReviewLikeView,
    BookReviewUserListView
)

urlpatterns = [
    path('<fk>', BookReviewListView.as_view(), name="reviewlist"),
    path('create/', BookReviewCreateView.as_view(), name='createreview'),
    path('like/<pk>', BookReviewLikeView.as_view(), name='likereview'),
    path('user/<fk>', BookReviewUserListView.as_view(), name="userreviewlist")
]
