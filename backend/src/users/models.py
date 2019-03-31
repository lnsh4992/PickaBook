from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, default="FirstName")
    last_name = models.CharField(max_length=20, default="LastName")
    review_count = models.IntegerField("Number of Reviews", default=0)
    creation_date= models.DateField(default=datetime.date.today)
    privacy= models.BooleanField(initial=False)
    bio = models.TextField("About me", max_length=500, default="Hey, Welcome to my Profile!")

    favorites = models.ManyToManyField('books.Book', related_name="favorites")
    following = models.ManyToManyField('authors.Author', related_name="following")

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
    avatar = models.ImageField(upload_to='user_avatar', blank=True, null=True, default='/user_avatar/logo.jpg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ProfilePicture(models.Model):
    avatar = models.ImageField(upload_to='user_avatar', blank=True)
