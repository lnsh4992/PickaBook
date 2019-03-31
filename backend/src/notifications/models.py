from django.db import models
import datetime

class Notification(models.Model):

    text = models.CharField(max_length=200, default='notification')
    creation_date= models.DateField(default=datetime.date.today)
    question = models.ForeignKey('qanswers.Question', on_delete=models.CASCADE, blank=True, null=True)
    isBook = models.IntegerField(default=1)
    prof = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.text
# Create your models here.
