from django.test import TestCase
from .models import Book
from django.urls import reverse
from django.utils import timezone

# Create your tests here.

def create_book(title, author_name):
    return Book.objects.create(title = title, author_name=author_name, publication_date=timezone.now())


# Model tests for books
class BookModelTest(TestCase):

    def test_book_creation(self):

        book_entry = create_book(title="t", author_name="a")
        self.assertTrue(isinstance(book_entry, Book))
        self.assertEqual(str(book_entry), book_entry.title)


# List view tests for books
class BookListTest(TestCase):

    def test_book_list_view(self):

        b1 = create_book(title="t1", author_name="a1")
        b2 = create_book(title="t2", author_name="a2")
        b3 = create_book(title='t3', author_name='a3')
        url = reverse('booklist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('t1', str(resp.content))
        self.assertIn('a1', str(resp.content))
        self.assertIn('t2', str(resp.content))
        self.assertIn('a2', str(resp.content))
        self.assertIn('t3', str(resp.content))
        self.assertIn('a3', str(resp.content))

    def test_book_title_order(self):

        b1 = create_book(title="Mistborn Archive", author_name="a1")
        b2 = create_book(title="All Great", author_name="a2")
        b3 = create_book(title='Brandon Sand', author_name='a3')
        url = reverse('booklist')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respContent = str(resp.content)

        self.assertTrue(respContent.find(b1.title) > respContent.find(b2.title))
        self.assertTrue(respContent.find(b1.title) > respContent.find(b3.title))
        self.assertTrue(respContent.find(b2.title) < respContent.find(b3.title))

    def test_book_substring(self):
        b1 = create_book(title="Mistborn Archive", author_name="a1")
        b2 = create_book(title="All Great", author_name="a2")
        b3 = create_book(title='Brandon Sand', author_name='a3')
        b4 = create_book(title="Born a bread", author_name="a4")
        b5 = create_book(title='bornity', author_name='a5')
        url = reverse('search', kwargs={'title': 'born'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respCon = str(resp.content)
        self.assertIn(b1.title, respCon)
        self.assertIn(b4.title, respCon)
        self.assertIn(b5.title, respCon)
        self.assertNotIn(b2.title, respCon)
        self.assertNotIn(b3.title, respCon)

    def test_book_substring_words(self):
        b1 = create_book(title="Mistborn Archive", author_name="1")
        b2 = create_book(title="All Grea", author_name="2")
        b3 = create_book(title='Brandon Sand', author_name='3')
        b4 = create_book(title="Born t bread", author_name="4")
        b5 = create_book(title='boarniy', author_name='5')
        url = reverse('search', kwargs={'title': 'born t'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respCon = str(resp.content)
        self.assertIn(b1.title, respCon)
        self.assertIn(b4.title, respCon)
        self.assertNotIn(b5.title, respCon)
        self.assertNotIn(b2.title, respCon)
        self.assertNotIn(b3.title, respCon)

    def test_book_substring_author(self):
        b1 = create_book(title="1", author_name="abc")
        b2 = create_book(title="2", author_name="xyz")
        b3 = create_book(title='3', author_name='abcde')
        b4 = create_book(title="4", author_name="ab cd")
        b5 = create_book(title='5', author_name='axbyzdec')
        url = reverse('search', kwargs={'title': 'abc'})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        respCon = str(resp.content)
        print(respCon)
        self.assertIn(b1.author_name, respCon)
        self.assertNotIn(b3.author_name, respCon)
        self.assertNotIn(b5.author_name, respCon)
        self.assertNotIn(b2.author_name, respCon)
        self.assertNotIn(b3.author_name, respCon)
