from django.urls import path, re_path

from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView,
    BookSearchView,
    BookAuthorView,
    BookSearchResultView
)

urlpatterns = [
    path('booklist/', BookListView.as_view(), name='booklist'),
    re_path(r'^search/(?P<title>[\w\s]+)$', BookSearchResultView.as_view(), name='search'),
    path('booklist/<pk>/', BookDetailView.as_view()),
    path('createbook/', BookCreateView.as_view()),
    re_path(r'^view/(?P<title>[\w\s]+)$', BookSearchView.as_view()),
    re_path(r'^authorbooks/(?P<author>[\w\s]+)$', BookAuthorView.as_view())
]