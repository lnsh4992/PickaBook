from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView
)
from books.models import Book
from .serializers import (
    BookSerializer,
    BookCreateSerializer
)
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer