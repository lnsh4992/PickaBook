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
