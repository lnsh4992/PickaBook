from rest_framework import serializers
from books.models import Book

class BookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title')

class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title', 'author_name', 'image_url')

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
        
