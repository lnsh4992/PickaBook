from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title', 'isbn', 'author_name', 'publication_date', 'genre', 'rating', 'number_of_reviews', 'image_url', 'synopsis')

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'author_name', 'publication_date', 'genre', 'rating', 'number_of_reviews', 'image_url', 'synopsis')

# class BookSearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('pk', 'title', 'author_name', 'publication_date', 'genre', 'rating', 'number_of_reviews', 'image_url', 'synopsis')
        
