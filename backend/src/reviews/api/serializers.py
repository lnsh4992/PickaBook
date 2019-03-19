from rest_framework import serializers
from reviews.models import BookReview
from users.api.serializers import ProfileShortSerializer

class BookReviewSerializer(serializers.ModelSerializer):
    prof = ProfileShortSerializer(many=False, read_only = True)

    class Meta:
        model = BookReview
        fields = ('pk', 'prof', 'book', 'title', 'content', 'rating', 'creation_date', 'likes', 'dislikes')


class BookReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ('likes', 'dislikes')

    def update(self, instance, validated_data):
        review = instance
        input = validated_data.pop('likes')
        
        
        if input == 1:
            review.likes += 1
        else:
            review.dislikes += 1

        review.save()
        return review
