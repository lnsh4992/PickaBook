# Generated by Django 2.1.5 on 2019-02-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190216_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FA', 'Fantasy'), ('RO', 'Romance'), ('TR', 'Thriller'), ('MY', 'Mystery'), ('BI', 'Biography'), ('FI', 'Fiction'), ('NF', 'Non Fiction'), ('SF', 'Science Fiction')], default='FA', max_length=2),
        ),
    ]
