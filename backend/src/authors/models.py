from django.db import models

# Create your models here.

class Author(models.Model):

    first_name = models.CharField(max_length=20, default="FirstName")
    last_name = models.CharField(max_length=20, default="LastName")
    review_count = models.IntegerField("Number of Reviews", default=0)
    bio = models.TextField("About me", max_length=500, default=str(first_name+last_name))
    #previousworks =
    genre = models.CharField(max_length=20, default="FA")

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
