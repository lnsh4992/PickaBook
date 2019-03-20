from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
import datetime
from users.models import Profile
# Create your models here.
 
class BookReview(models.Model):
    prof = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=120, blank=False)
    content = models.TextField(max_length=500, blank=False)
    rating = models.FloatField(default=0.0)

    creation_date= models.DateField(default=datetime.date.today)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title    

    def save(self, *args, **kwargs):
        profx = self.prof
#        self.prof.review_count = self.prof.review_count + 1
#        self.prof.save()
        super().save(*args, **kwargs)
        revs = BookReview.objects.filter(book=self.book)
        avg = revs.aggregate(Avg('rating'))['rating__avg']
#        print(avg)
        self.book.rating = avg
        self.book.number_of_reviews = self.book.number_of_reviews + 1 
        self.book.save()