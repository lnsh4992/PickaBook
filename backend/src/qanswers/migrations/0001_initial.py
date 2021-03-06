# Generated by Django 2.1.5 on 2019-02-17 05:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0006_auto_20190216_2306'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=500)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=300)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qanswers.Question'),
        ),
    ]
