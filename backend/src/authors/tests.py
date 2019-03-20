from django.test import TestCase
from .models import Author
from django.urls import reverse
from django.utils import timezone

# Create your tests here.
def create_author(name):
    return Author.objects.create(name=name)


# Model tests for books
class AuthorModelTest(TestCase):

    def test_author_creation(self):

        auth_entry = create_author(name="author-1")
        self.assertTrue(isinstance(auth_entry, Author))
        self.assertEqual(str(auth_entry), auth_entry.name)