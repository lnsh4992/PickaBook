# Generated by Django 2.1.5 on 2019-04-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_book_isbn'),
        ('users', '0009_profile_isprivate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommended',
            field=models.ManyToManyField(related_name='recommended', to='books.Book'),
        ),
    ]
