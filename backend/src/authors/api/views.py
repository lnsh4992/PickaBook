from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from authors.models import Author
from .serializers import AuthorSerializer

class AuthorWorktView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
