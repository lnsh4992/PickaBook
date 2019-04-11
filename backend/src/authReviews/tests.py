from django.test import TestCase
from .models import AuthorReview
from authors.models import Author
from users.models import Profile
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode


# Create your tests here.

class AuthorReviewModelTest(TestCase):

    def create_review(self, username='Review test user', likes=0):
        
        newuser = User.objects.create(username=username, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        newAuthor = Author.objects.create(name="Review test author")
        return AuthorReview.objects.create(prof=newProf, likes=likes, author=newAuthor, title="Reviw test title", content="Review test content")

    def create_prof(self, uname='Review test user'):
        newuser = User.objects.create(username=uname, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        return newProf        

    def create_author(self):
        return Author.objects.create(name="Review Test Author")

    def create_review_for_author(self, prof, author, likes=0):
        return AuthorReview.objects.create(prof=prof, likes=likes, author=author, title="Reviw test title", content="Review test content")

    def test_author_review_creation(self):

        review_entry = self.create_review()
        self.assertTrue(isinstance(review_entry, AuthorReview))
        self.assertEqual(str(review_entry), review_entry.title)

    def test_author_review_list(self):

        review_entry = self.create_review()
        url = reverse('authreviewlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(review_entry.content, str(resp.content))

    def test_author_review_driver_create(self):
        newProf = self.create_prof()
        author = self.create_author()
        
        url = reverse('authcreatereview')
        resp = self.client.post(url, {
                        'title': 'revTitle',
                        'content': 'revCont',
                        'rating': '3.5',
                        'prof': newProf.pk,
                        'author': author.pk
                })

        self.assertEqual(resp.status_code, 201)

        review = AuthorReview.objects.get(pk=1)
        self.assertEqual(review.title, 'revTitle')

    def test_author_review_rating_driver(self):
        newProf = self.create_prof()
        author = self.create_author()
        
        url = reverse('authcreatereview')
        resp = self.client.post(url, {
                        'title': 'revTitle',
                        'content': 'revCont',
                        # 'rating': '5.0',
                        'prof': newProf.pk,
                        'author': author.pk
                })

        self.assertEqual(resp.status_code, 201)

        review = AuthorReview.objects.get(pk=1)
        self.assertEqual(review.title, 'revTitle')
        # author = Author.objects.get(pk=author.pk)
        # self.assertEqual(author.rating, 5.0)

        resp = self.client.post(url, {
                        'title': 'revTitle2',
                        'content': 'revCont2',
                        # 'rating': '3.0',
                        'prof': newProf.pk,
                        'author': author.pk
                })

        self.assertEqual(resp.status_code, 201)
        review = AuthorReview.objects.get(pk=2)
        self.assertEqual(review.title, 'revTitle2')
        # author = Author.objects.get(pk=author.pk)
        # self.assertEqual(author.rating, 4.0)

    def test_author_review_like(self):

        review = self.create_review()
        url = reverse('authlikereview', kwargs={'pk': review.pk})
        resp = self.client.put(url, 
                                data = urlencode({'likes': '1'}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)

        review = AuthorReview.objects.get(pk=review.pk)

        self.assertEqual(review.likes, 1)
        self.assertEqual(review.dislikes, 0)

    def test_author_review_dislike(self):

        review = self.create_review()

        url = reverse('authlikereview', kwargs={'pk': review.pk})
        resp = self.client.put(url, 
                                data = urlencode({'likes': 0}),
                                content_type = 'application/x-www-form-urlencoded'
                            )

        self.assertEqual(resp.status_code, 200)

        review = AuthorReview.objects.get(pk=review.pk)
        self.assertEqual(review.dislikes, 1)
        self.assertEqual(review.likes, 0)

    def test_author_review_sorted(self):
        u1 = self.create_prof('u1')
        u2 = self.create_prof('u2')
        author = self.create_author()
        r1 = self.create_review_for_author(u1, author, 6)
        r2 = self.create_review_for_author(u2, author, 2)
        r3 = self.create_review_for_author(u2, author, 4)
        r4 = self.create_review_for_author(u1, author, 0)

        url = reverse('authreviewlist', kwargs={'fk': author.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respContent = str(resp.content)
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r2.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r3.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r1.likes)) < respContent.find("\"likes\":"+str(r4.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r4.likes)) > respContent.find("\"likes\":"+str(r2.likes)))
        self.assertTrue(respContent.find("\"likes\":"+str(r4.likes)) > respContent.find("\"likes\":"+str(r3.likes)))
        