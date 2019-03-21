from django.test import TestCase
from .models import (
    Question,
    Answer
)
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from books.models import Book
# Create your tests here.

class QATest(TestCase):
    def create_question(self, username="user1", password="secret"):
        newuser = User.objects.create(username=username, password=password)
        newProf = Profile.objects.get(user=newuser)
        newBook = Book.objects.create(title="bookexample")
        quesn = Question.objects.create(profile=newProf, book=newBook, question="test??")
        return quesn, newProf, newBook

    def create_answer(self):
        quesn, newProf, newBook = self.create_question()
        answer = Answer.objects.create(profile=newProf, question=quesn, book=newBook, answer="test." )
        return answer, quesn

    
    def create_prof(self, uname='Review test user'):
        newuser = User.objects.create(username=uname, password="Secret")
        newProf = Profile.objects.get(user=newuser)
        return newProf        

    def create_book(self):
        return Book.objects.create(title="Review Test Book")

    def test_question_creation(self):
        a, _, __ = self.create_question()
        self.assertTrue(isinstance(a, Question))
        
    def test_answer_creation(self):
        answer, question = self.create_answer()
        self.assertTrue(isinstance(answer, Answer))

    def test_question_answer_key(self):
        a, q = self.create_answer()
        self.assertTrue((a.question.pk == q.pk))

    def test_question_list_view(self):
        q, _, __ = self.create_question()
        url = reverse('questionlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(q.question, str(resp.content))

    def test_answer_list_view(self):
        a, q = self.create_answer()
        url = reverse('answerlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.answer, str(resp.content))
    
    def test_question_answer_list_view(self):
        a, q = self.create_answer()
        url = reverse('questionlist', kwargs={'fk': 1})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(q.question, str(resp.content))
        self.assertIn(a.answer, str(resp.content))
    
    def test_create_question_driver(self):
        newProf = self.create_prof()
        book = self.create_book()
        
        url = reverse('questioncreate')

        resp = self.client.post(url, {
                        'question': 'questionTitle',
                        'profile': str(newProf.pk),
                        'book': str(book.pk)
                })

        self.assertEqual(resp.status_code, 201)

        question = Question.objects.get(pk=1)
        self.assertEqual(question.question, 'questionTitle')

    def test_create_answer_driver(self):
        q, p, b = self.create_question()

        url = reverse('answercreate')
        resp = self.client.post(url, {
                    'question': q.pk,
                    'profile': p.pk,
                    'book': b.pk,
                    'answer': 'answerTest'
        })
        self.assertEqual(resp.status_code, 201)
        answer = Answer.objects.get(pk=1)
        self.assertEqual(answer.answer, 'answerTest')

    def test_question_answer_serializer_driver(self):
        newProf = self.create_prof()
        newProf2 = self.create_prof(uname='prof2')
        book = self.create_book()
        
        url = reverse('questioncreate')

        resp = self.client.post(url, {
                        'question': 'questionTitle',
                        'profile': str(newProf.pk),
                        'book': str(book.pk)
                })

        self.assertEqual(resp.status_code, 201)

        question = Question.objects.get(pk=1)
        self.assertEqual(question.question, 'questionTitle')

        url = reverse('answercreate')
        resp = self.client.post(url, {
                    'question': question.pk,
                    'profile': newProf.pk,
                    'book': book.pk,
                    'answer': 'answerTest1'
        })
        self.assertEqual(resp.status_code, 201)
        answer1 = Answer.objects.get(pk=1)
        self.assertEqual(answer1.answer, 'answerTest1')

        resp = self.client.post(url, {
                    'question': question.pk,
                    'profile': newProf2.pk,
                    'book': book.pk,
                    'answer': 'answerTest2'
        })
        self.assertEqual(resp.status_code, 201)
        answer2 = Answer.objects.get(pk=2)
        self.assertEqual(answer2.answer, 'answerTest2')

        url = reverse('questionlist', kwargs={'fk': book.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(question.question, str(resp.content))
        self.assertIn(answer1.answer, str(resp.content))
        self.assertIn(answer2.answer, str(resp.content))


