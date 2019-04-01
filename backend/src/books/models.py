from django.db import models
from django.core.exceptions import ValidationError
from notifications.models import Notification
from authors.models import Author

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

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)
        auth = None
        try:
            auth = Author.objects.get(name=self.author_name)
        except Author.DoesNotExist:
            auth = None
        
        if auth is not None:
            profs = auth.following.all()
            notif = self.author_name + " has released a new Book! Check out " + self.title
            for prof in profs:
                Notification.objects.create(text=notif, book=self, isBook=1, prof=prof)

        