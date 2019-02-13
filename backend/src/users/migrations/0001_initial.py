# Generated by Django 2.1.5 on 2019-02-13 00:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='FirstName', max_length=20)),
                ('last_name', models.CharField(default='LastName', max_length=20)),
                ('review_count', models.IntegerField(default=0, verbose_name='Number of Reviews')),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('bio', models.TextField(default='Hey, Welcome to my Profile!', max_length=500, verbose_name='About me')),
                ('genre', models.CharField(choices=[('FA', 'Fantasy'), ('RO', 'Romance'), ('TR', 'Thriller'), ('MY', 'Mystery'), ('BI', 'Biography'), ('FI', 'Fiction'), ('NF', 'Non Fiction'), ('SF', 'Science Fiction')], default='FA', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]