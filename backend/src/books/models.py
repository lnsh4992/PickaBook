from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Book(models.Model):

    # title of the book
    title = models.CharField(max_length=200, unique=True)

    # ISBN Code
    isbn = models.CharField(max_length=10, default = 'XXXXXXXXXX')
    
    # author of the book
    author_name = models.CharField(max_length=100, default = '')
    
    # publication date
    publication_date = models.DateField(null=True)
    
    # genre
    GENRES = (
        ('FA', 'Fantasy'),
        ('RO', 'Romance'),
        ('TR', 'Thriller'),
        ('MY', 'Mystery'),
        ('BI', 'Biography'),
        ('FI', 'Fiction'),
        ('NF', 'Non Fiction'),
        ('SF', 'Science Fiction'),
    )

    genre = models.CharField(max_length=2, choices = GENRES, default='FA')

    # rating
    rating = models.FloatField(default=0.0)

    # number of reviews
    number_of_reviews = models.IntegerField(default=0)

    # image
    image_url = models.CharField(max_length=200, default = '')
    
    # synopsis/blurb
    synopsis = models.TextField(null=True, blank=True)



    def __str__(self):
        return self.title