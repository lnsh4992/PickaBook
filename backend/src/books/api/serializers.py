from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author_name', 'publication_date', 'genre', 'rating', 'number_of_reviews', 'image_url', 'synopsis')