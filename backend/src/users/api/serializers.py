from rest_framework import serializers
from users.models import Profile
from books.api.serializers import BookSerializer

class ProfileSerializer(serializers.ModelSerializer):
    favorites = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Profile 
        fields = ('pk', 'first_name', 'last_name', 'review_count', 'creation_date', 'bio', 'genre', 'favorites')

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'genre')
        read_only_fields = ['user', 'review_count', 'creation_date']

class ProfileAddFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('favorites',)
        
    def update(self, instance, validated_data):
        prof = instance
        favBooks = validated_data.pop('favorites')
        for book in favBooks:
            prof.favorites.add(book)
        prof.save()
        return prof

class ProfileAddFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('following',)

    def update(self, instance, validated_data):
        prof = instance
        print(validated_data)
        following = validated_data.pop('following')
        for author in following:
            prof.following.add(author)
        prof.save()
        return prof