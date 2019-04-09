from rest_framework import permissions
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView
)

from reviews.models import BookReview
from .serializers import (
    BookReviewSerializer,
    BookReviewLikeSerializer,
    BookReviewCreateSerializer,
    BookReviewProfileSerializer
)

class BookReviewCreateView(CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewCreateSerializer

class BookReviewListView(ListAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer

    def get_queryset(self):
        return BookReview.objects.filter(book=self.kwargs['fk']).order_by('-likes')


class BookReviewLikeView(UpdateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewLikeSerializer

class BookReviewUserListView(ListAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewProfileSerializer

    def get_queryset(self):
        return BookReview.objects.filter(prof=self.kwargs['fk']).order_by('-likes')