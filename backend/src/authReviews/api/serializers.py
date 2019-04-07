from rest_framework import serializers
from authReviews.models import AuthorReview
from users.api.serializers import ProfileShortSerializer

class AuthorReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorReview
        fields = ('pk', 'prof', 'author', 'title', 'content', 'rating', 'creation_date', 'likes', 'dislikes')

class AuthorReviewSerializer(serializers.ModelSerializer):
    prof = ProfileShortSerializer(many=False, read_only = True)

    class Meta:
        model = AuthorReview
        fields = ('pk', 'prof', 'author', 'title', 'content', 'rating', 'creation_date', 'likes', 'dislikes')


class AuthorReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorReview
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
