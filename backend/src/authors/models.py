from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length=50, default="Name")
    #last_name = models.CharField(max_length=20, default="LastName")
    review_count = models.IntegerField("Number of Reviews", default=0)
    bio = models.TextField("About me", max_length=500, default=str(first_name + "  "+ last_name))
    previousworks = (('BOOK NAME', 'Description'))
    genre = models.CharField(max_length=20, default="FA")
    review = models.DecimalField(min_value=0.0, max_value=5.0)

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
