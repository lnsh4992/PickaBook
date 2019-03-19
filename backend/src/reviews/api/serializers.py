from rest_framework import serializers
from reviews.models import BookReview
from users.api.serializers import ProfileShortSerializer

class BookReviewSerializer(serializers.ModelSerializer):
    prof = ProfileShortSerializer(many=False, read_only = True)

    class Meta:
        model = BookReview
        fields = ('pk', 'prof', 'book', 'title', 'content', 'rating', 'creation_date', 'likes', 'dislikes')
