# Generated by Django 5.1.5 on 2025-01-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=100),
        ),
    ]
