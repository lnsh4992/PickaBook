from rest_framework import permissions
from django.shortcuts import get_object_or_404


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView
)

from authReviews.models import AuthorReview
from .serializers import (
    AuthorReviewSerializer,
    AuthorReviewLikeSerializer,
    AuthorReviewCreateSerializer,
    AuthorReviewProfileSerializer
)

class AuthorReviewCreateView(CreateAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewCreateSerializer

class AuthorReviewListView(ListAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewSerializer

    def get_queryset(self):
        return AuthorReview.objects.filter(author=self.kwargs['fk']).order_by('-likes')

class AuthorReviewLikeView(UpdateAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewLikeSerializer

class AuthorReviewUserListView(ListAPIView):
    queryset = AuthorReview.objects.all()
    serializer_class = AuthorReviewProfileSerializer

    def get_queryset(self):
        return AuthorReview.objects.filter(prof=self.kwargs['fk']).order_by('-likes')