from django.urls import path

from .views import (
    AuthorDetailView,
    #AuthorListView
)

urlpatterns = [
    #path('', AuthorListView.as_view()),
    path(r'^view/(?P<name>[\w\s]+)$', AuthorDetailView.as_view())
]
