from django.test import TestCase
from .models import Notification
from books.models import Book
from authors.models import Author
from users.models import Profile
from qanswers.models import Question, Answer
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode

# Create your tests here.

class NotificationTest(TestCase):

    def create_prof(self, uname='Review test user'):
        newuser = User.objects.create(username=uname, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        newProf.first_name = uname
        newProf.save()
        return newProf        

    def create_book(self):
        return Book.objects.create(title="Notification Test Book")

    def book_from_author(self, authname, title="Notification Test Book"):
        return Book.objects.create(title=title, author_name=authname)

    def create_notification(self, text="Test Notif"):
        prof = self.create_prof()
        book = self.create_book()

        return Notification.objects.create(text=text, prof=prof, book=book)

    def create_notification_prof_book(self, prof, book, text="Test Notif"):
        return Notification.objects.create(text=text, prof=prof, book=book)

    def test_notification_creation(self):

        notification_entry = self.create_notification()
        self.assertTrue(isinstance(notification_entry, Notification))
        self.assertEqual(str(notification_entry), notification_entry.text)

    def test_notification_list(self):

        notification_entry = self.create_notification()
        url = reverse('notificationlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(notification_entry.text, str(resp.content))

    def test_notification_sorted(self):
        u1 = self.create_prof('u1')
        book = self.create_book()
        n1 = self.create_notification_prof_book(u1, book, "notif1")
        n2 = self.create_notification_prof_book(u1, book, "notif2")
        n3 = self.create_notification_prof_book(u1, book, "notif3")

        url = reverse('notificationlist', kwargs={'fk': u1.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respContent = str(resp.content)
        self.assertTrue(respContent.find("\"likes\":"+str(n1.creation_date)) <= respContent.find("\"likes\":"+str(n2.creation_date)))
        self.assertTrue(respContent.find("\"likes\":"+str(n1.creation_date)) <= respContent.find("\"likes\":"+str(n3.creation_date)))
        self.assertTrue(respContent.find("\"likes\":"+str(n2.creation_date)) <= respContent.find("\"likes\":"+str(n3.creation_date)))

    def test_notification_delete(self):
        n = self.create_notification()
        self.assertTrue(isinstance(n, Notification))

        url = reverse('destroynotification', kwargs={'pk': n.pk})
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)

        objs = Notification.objects.all()
        self.assertTrue(objs.count() == 0)
        
    def test_notification_author(self):
        prof = self.create_prof()
        auth = Author.objects.create(name='testauth')
        prof.following.add(auth)
        prof.save()

        book = self.book_from_author(auth.name)
        objs = Notification.objects.all()
        self.assertEqual(objs.count(), 1)

    def test_notification_author_many(self):
        profs = []
        profs.append(self.create_prof('u1'))
        profs.append(self.create_prof('u2'))
        profs.append(self.create_prof('u3'))
        profs.append(self.create_prof('u4'))
        auth = Author.objects.create(name='testauth')
        for prof in profs:
            prof.following.add(auth)
            prof.save()

        book = self.book_from_author(auth.name)
        objs = Notification.objects.all()
        self.assertEqual(objs.count(), len(profs))

        book = self.book_from_author(auth.name, "book2")
        objs = Notification.objects.all()
        self.assertEqual(objs.count(), 2*len(profs))
        
    def test_notification_answer(self):
        prof1 = self.create_prof('u1')
        book = self.create_book()
        q1 = Question.objects.create(profile=prof1, book=book, question="test")
        prof2 = self.create_prof('u2')
        a1 = Answer.objects.create(profile=prof2, book=book, question=q1, answer='testing')

        objs = Notification.objects.all()
        self.assertEqual(objs.count(), 1)

        notif = objs[0]
        self.assertTrue(prof2.first_name in notif.text)
        self.assertEqual(notif.prof, prof1)
        self.assertEqual(notif.book, book)
        self.assertEqual(notif.isBook, 0)

    def test_notification_answer_many(self):
        prof1 = self.create_prof('u1')
        book = self.create_book()
        q1 = Question.objects.create(profile=prof1, book=book, question="test")
        prof2 = self.create_prof('u2')
        prof3 = self.create_prof('u3')
        a1 = Answer.objects.create(profile=prof2, book=book, question=q1, answer='testing1')
        a2 = Answer.objects.create(profile=prof2, book=book, question=q1, answer='testing2')
        a3 = Answer.objects.create(profile=prof3, book=book, question=q1, answer='testing3')

        objs = Notification.objects.all()
        self.assertEqual(objs.count(), 3)    

        url = reverse('notificationlist', kwargs={'fk': prof1.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(prof2.first_name, str(resp.content))
        self.assertIn(prof3.first_name, str(resp.content))
        self.assertIn(book.title, str(resp.content))
