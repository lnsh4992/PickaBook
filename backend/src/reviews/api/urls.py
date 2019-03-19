from django.urls import path

from .views import (
    BookReviewCreateView,
    BookReviewListView,
    BookReviewLikeView
)

urlpatterns = [
    path('<fk>', BookReviewListView.as_view(), name="reviewlist"),
    path('create/', BookReviewCreateView.as_view()),
    path('like/<pk>', BookReviewLikeView.as_view())
    
]