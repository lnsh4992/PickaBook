from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView
)
from books.models import Book
from .serializers import (
    BookSerializer,
    BookCreateSerializer,
    # BookSearchSerializer
)
from .search import search

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by('title')

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookSearchView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'title'

class BookSearchResultView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        response = search(self.kwargs['title'])
        return response
        # print(response)

class BookAuthorView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(author_name=self.kwargs['author'])

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer