from rest_framework import serializers
from users.models import Profile, ProfilePicture
from authors.models import Author
from books.models import Book
from books.api.serializers import (
    BookSerializer,
    BookTitleSerializer
)
from authors.api.serializers import AuthorCardSerializer
from authors.api.serializers import AuthorNameSerializer

class ProfileSerializer(serializers.ModelSerializer):
    favorites = BookSerializer(read_only=True, many=True)
    following = AuthorCardSerializer(read_only=True, many=True)
    recommended = BookSerializer(read_only=True, many=True)

    class Meta:
        model = Profile 
        fields = ('pk', 'first_name', 'last_name', 'isPrivate', 'review_count', 'creation_date', 'bio', 'genre', 'favorites', 'following', 'recommended', 'avatar')

class ProfileShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'first_name', 'last_name', 'avatar', 'review_count')

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
        fields = ('first_name', 'last_name', 'bio', 'genre', 'isPrivate', 'avatar')
        read_only_fields = ['user', 'review_count', 'creation_date']

class ProfileRemoveRecommendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('recommended',)

    def update(self, instance, validated_data):
        prof = instance
        recBooks = validated_data.pop('recommended')
        for book in recBooks:
            prof.recommended.remove(book)

        prof.save()
        return prof

class ProfileAddFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('favorites',)
        
    def update(self, instance, validated_data):
        prof = instance
        flag = False
        favBooks = validated_data.pop('favorites')
        for book in favBooks:
            if book in prof.favorites.all():
                prof.favorites.remove(book)
            else:
                prof.favorites.add(book)
                flag = True
        
        if not flag:
            prof.save()
            return prof

        usrs = Profile.objects.all()
        profFav = prof.favorites.all()
        max = 0
        qset = None
        for usr in usrs:
            if(usr == prof):
                continue
            usrFav = usr.favorites.all()
            intersection = profFav & usrFav
            if(intersection.count()  > max):
                max = intersection.count()
                qset = usrFav.difference(profFav)

        if(max > 0):
            prof.recommended.add(*qset)
        
        prof.save()
        return prof



class ProfileAddFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('following',)

    def update(self, instance, validated_data):
        prof = instance
        flag = False

        following = validated_data.pop('following')
        for author in following:
            if author in prof.following.all():
                prof.following.remove(author)
                author.numFollowers -= 1
            else:
                prof.following.add(author)
                author.numFollowers += 1
                flag = True
            author.save()

        if not flag:
            prof.save()
            return prof

        profFol = prof.following.all()
        profFav = prof.favorites.all()
        usrs = Profile.objects.all()
        max = 0
        qset = None
        
        for usr in usrs:
            if (usr == prof):
                continue
            usrFol = usr.following.all()
            intersection = usrFol & profFol
            if( intersection.count() > max):
                max = intersection.count()
                qset = usrFol.difference(profFol)

        if( max == 0):
            prof.save()
            return prof

        newBooks = Book.objects.none()
        for auth in qset:
            authBooks = Book.objects.filter(author_name=auth.name)
            newBooks = newBooks.union(authBooks)
            
        prof.recommended.add(*newBooks)
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