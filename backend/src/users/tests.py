from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from books.models import Book
from authors.models import Author
from django.utils import timezone
from django.db.utils import IntegrityError
from django.urls import reverse
from  .api.views import ProfileDetailView 
from urllib.parse import urlencode

# Create your tests here.

class ProfileTest(TestCase):
    def create_profile(self, username="user1", password="secret"):
        newuser = User.objects.create(username=username, password=password)
        newProf = Profile.objects.get(user=newuser)
        return newProf

    def create_book(self, title='book', author_name='Author'):
        return Book.objects.create(title = title, author_name=author_name, publication_date=timezone.now())

    def create_author(self, name='Author'):
        return Author.objects.create(name=name)

    def test_profile_creation(self):
        a = self.create_profile()
        self.assertTrue(isinstance(a, Profile))

    def test_profile_onetoone(self):
        a = self.create_profile()
        userid = a.user
        #OnetoOne Test
        self.assertTrue((User.objects.filter(pk=userid.pk).count() == 1))

    def test_unique_email(self):
        user1 = User.objects.create(username='user2', password='secret', email='test@gmail.com')
        with self.assertRaises(IntegrityError):
            user2 = User.objects.create(username='user3', password='secret', email='test@gmail.com')

    def test_profile_detail_view(self):

        user3 = User.objects.create(username='user4', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user3)
        url = reverse('userprofiledetail', kwargs={'user__pk': user3.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(prof.first_name, str(resp.content))

    def test_author_follow(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        auth = self.create_author()
        auth2 = self.create_author(name='auth2')
        prof.following.add(auth)
        prof.following.add(auth2)
        prof.save()
        self.assertTrue(auth in prof.following.all())
        self.assertTrue(auth2 in prof.following.all())

        prof.following.remove(auth)
        prof.save()
        self.assertTrue(auth not in prof.following.all())
        self.assertTrue(auth2 in prof.following.all())

    def test_author_unfollow(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        auth = self.create_author()
        auth2 = self.create_author(name='auth2')
        prof.following.add(auth)
        prof.following.add(auth2)
        prof.save()
        self.assertTrue(auth in prof.following.all())
        self.assertTrue(auth2 in prof.following.all())

        authID = auth.pk
        auth_remove = Author.objects.get(pk=authID)

        if auth_remove in prof.following.all():
            prof.following.remove(auth_remove)
            prof.save()

        self.assertTrue(auth not in prof.following.all())
        self.assertTrue(auth2 in prof.following.all())        
        
    def test_unfollow_driver(self):
        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        auth = self.create_author()
        auth2 = self.create_author(name='auth2')
        prof.following.add(auth)
        prof.following.add(auth2)
        prof.save()
        self.assertTrue(auth in prof.following.all())
        self.assertTrue(auth2 in prof.following.all())

        authID = auth.pk

        url = reverse('followauthor', kwargs={'pk': prof.pk, })
        resp = self.client.put(url, 
                                data = urlencode({'following': str(authID)}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(auth not in prof.following.all())
        

    def test_get_all_authors(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        auths = []
        for i in range(6):
            auths.append(self.create_author(name='auth'+str(i)))

        for i in range(5):
            prof.following.add(auths[i])
        prof.save()

        for i in range(5):
            self.assertTrue(auths[i] in prof.following.all())
        self.assertTrue(auths[5] not in prof.following.all())

    def test_book_favorite(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        book = self.create_book()
        book2 = self.create_book(title='book2')
        prof.favorites.add(book)
        prof.favorites.add(book2)
        prof.save()
        self.assertTrue(book in prof.favorites.all())
        self.assertTrue(book2 in prof.favorites.all())

        prof.favorites.remove(book)
        prof.save()
        self.assertTrue(book not in prof.favorites.all())
        self.assertTrue(book2 in prof.favorites.all())       

    def test_book_unfavorite(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        book = self.create_book()
        book2 = self.create_book(title='book2')
        prof.favorites.add(book)
        prof.favorites.add(book2)
        prof.save()
        self.assertTrue(book in prof.favorites.all())
        self.assertTrue(book2 in prof.favorites.all())

        bookID = book.pk
        book_remove = Book.objects.get(pk=bookID)

        if book_remove in prof.favorites.all():
            prof.favorites.remove(book_remove)
            prof.save()

        self.assertTrue(book not in prof.favorites.all())
        self.assertTrue(book2 in prof.favorites.all())        

    def test_unfavorite_driver(self):
        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        book = self.create_book()
        book2 = self.create_book(title='book2')
        prof.favorites.add(book)
        prof.favorites.add(book2)
        prof.save()
        self.assertTrue(book in prof.favorites.all())
        self.assertTrue(book2 in prof.favorites.all())

        bookID = book.pk

        url = reverse('favoritebook', kwargs={'pk': prof.pk, })
        resp = self.client.put(url, 
                                data = urlencode({'favorites': str(bookID)}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(book not in prof.favorites.all())


    def test_get_all_books(self):

        user = User.objects.create(username='user5', password='secret', email='test@gmail.com')
        prof = Profile.objects.get(user=user)
        books = []
        for i in range(6):
            books.append(self.create_book(title='book'+str(i)))

        for i in range(5):
            prof.favorites.add(books[i])
        prof.save()

        for i in range(5):
            self.assertTrue(books[i] in prof.favorites.all())
        self.assertTrue(books[5] not in prof.favorites.all())
