from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=50, default="Name")
    #last_name = models.CharField(max_length=20, default="LastName")
    birthdate = models.DateField(null=True)
    image_url = models.CharField(max_length=200, default = '')
    review_count = models.IntegerField("Number of Reviews", default=0)
    bio = models.TextField("About me", max_length=500, default=name)
    previousworks = (('BOOK NAME', 'Description'))
    #previousworks = models.ListCharField(
#        title = models.CharField(max_length=50, default="Book Name"),
#        desc = models.TextField("Book Description", max_length=100, default="About Book")
        #size = 100,
#    )
    numFollowers = models.IntegerField(default=0)

    #genre = models.CharField(max_length=20, default="FA")

    review = models.DecimalField(max_digits=4,decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)

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

    def __str__(self):
        return self.name