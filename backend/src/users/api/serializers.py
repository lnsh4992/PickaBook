from rest_framework import serializers
from users.models import Profile, ProfilePicture
from authors.models import Author
from books.api.serializers import (
    BookSerializer,
    BookTitleSerializer
)
from authors.api.serializers import AuthorCardSerializer
from authors.api.serializers import AuthorNameSerializer

class ProfileSerializer(serializers.ModelSerializer):
    favorites = BookSerializer(read_only=True, many=True)
    following = AuthorCardSerializer(read_only=True, many=True)

    class Meta:
        model = Profile 
        fields = ('pk', 'first_name', 'last_name', 'review_count', 'creation_date', 'bio', 'genre', 'favorites', 'following', 'avatar')

class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'first_name', 'last_name', 'avatar')

class ProfileFavoriteSerializer(serializers.ModelSerializer):
    favorites = BookTitleSerializer(read_only=True, many=True)
    class Meta:
        model = Profile
        fields = ('pk', 'favorites')

class ProfileFollowingSerializer(serializers.ModelSerializer):
    following = AuthorNameSerializer(read_only=True, many=True)
    class Meta:
        model = Profile
        fields = ('pk', 'following')

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'genre', 'avatar')
        read_only_fields = ['user', 'review_count', 'creation_date']

class ProfileAddFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('favorites',)
        
    def update(self, instance, validated_data):
        prof = instance
        favBooks = validated_data.pop('favorites')
        for book in favBooks:
            if book in prof.favorites.all():
                prof.favorites.remove(book)
            else:
                prof.favorites.add(book)
        prof.save()
        return prof

class ProfileAddFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('following',)

    def update(self, instance, validated_data):
        prof = instance

        following = validated_data.pop('following')
        for author in following:
            if author in prof.following.all():
                prof.following.remove(author)
                author.numFollowers -= 1
            else:
                prof.following.add(author)
                author.numFollowers += 1
            author.save()
        prof.save()
        return prof

class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', )


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['avatar', ]