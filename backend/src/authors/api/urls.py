from django.urls import path

from .views import (
    AuthorDetailView,
    AuthorListView
)

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('author<str:author>', AuthorDetailView.as_view())
]
