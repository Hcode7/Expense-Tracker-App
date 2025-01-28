from django.test import TestCase
from .models import Category, Book

# Create your tests here.

class CategoryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name='python',
            description='programming language'
        )

    def test_fileds(self):
        self.assertIsInstance(self.category.name, str)
        self.assertIsInstance(self.category.description, str)


class BookTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='python')
        Book.objects.create(
            book_id='1', 
            title='unit test', 
            subtitle='testing and debuging', 
            authors='amine', publisher='RATIT GROUP', 
            published_date='1/28/2025', 
            category=self.category, 
            distribution_expense=9.8
        )
    def test_book_creation(self):
        self.book = Book.objects.get(id=1)
        self.assertEqual(self.book.category.name, 'python')
        self.assertEqual(self.book.title, 'unit test')
        self.assertEqual(str(self.book), 'Book unit test by amine')
