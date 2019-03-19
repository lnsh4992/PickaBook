from django.test import TestCase
from .models import BookReview
from books.models import Book
from users.models import Profile
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode


# Create your tests here.

class BookReviewModelTest(TestCase):

    def create_review(self, username='Review test user', likes=0):
        
        newuser = User.objects.create(username=username, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        newBook = Book.objects.create(title="Review test book")
        return BookReview.objects.create(prof=newProf, likes=likes, book=newBook, title="Reviw test title", content="Review test content")

    def create_prof(self, uname='Review test user'):
        newuser = User.objects.create(username=uname, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        return newProf        

    def create_book(self):
        return Book.objects.create(title="Review Test Book")

    def create_review_for_book(self, prof, book, likes=0):
        return BookReview.objects.create(prof=prof, likes=likes, book=book, title="Reviw test title", content="Review test content")

    def test_review_creation(self):

        review_entry = self.create_review()
        self.assertTrue(isinstance(review_entry, BookReview))
        self.assertEqual(str(review_entry), review_entry.title)

    def test_review_list(self):

        review_entry = self.create_review()
        url = reverse('reviewlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(review_entry.content, str(resp.content))

    def test_review_like(self):

        review = self.create_review()
        url = reverse('likereview', kwargs={'pk': review.pk})
        resp = self.client.put(url, 
                                data = urlencode({'likes': '1'}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)

        review = BookReview.objects.get(pk=review.pk)

        self.assertEqual(review.likes, 1)
        self.assertEqual(review.dislikes, 0)


    def test_review_dislike(self):

        review = self.create_review()
        url = reverse('likereview', kwargs={'pk': review.pk})
        resp = self.client.put(url, 
                                data = urlencode({'likes': 0}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)

        review = BookReview.objects.get(pk=review.pk)
        self.assertEqual(review.dislikes, 1)
        self.assertEqual(review.likes, 0)

    def test_review_sorted(self):
        u1 = self.create_prof('u1')
        u2 = self.create_prof('u2')
        book = self.create_book()
        r1 = self.create_review_for_book(u1, book, 6)
        r2 = self.create_review_for_book(u2, book, 2)
        r3 = self.create_review_for_book(u2, book, 4)
        r4 = self.create_review_for_book(u1, book, 0)


        url = reverse('reviewlist', kwargs={'fk': book.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respContent = str(resp.content)
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r2.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r3.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r4.likes)))

        self.assertTrue(respContent.find("\"likes\":"+str(r4.likes)) > respContent.find("\"likes\":"+str(r2.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r4.likes)) > respContent.find("\"likes\":"+str(r3.likes)))
        