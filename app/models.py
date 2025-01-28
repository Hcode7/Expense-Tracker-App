from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=300)
    authors = models.CharField(max_length=150)
    publisher = models.CharField(max_length=250)
    published_date = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Book {self.title} by {self.authors}"