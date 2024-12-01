from django.test import TestCase
from .models import Book, Author

class BookTestCase(TestCase):
    def setUp(self):
        
        author1 = Author.objects.create(name='F. Scott Fitzgerald')
        author2 = Author.objects.create(name='Harper Lee')
        
        Book.objects.create(title='The Great Gatsby', author=author1, publication_year=1925)
        Book.objects.create(title='To Kill a Mockingbird', author=author2, publication_year=1960)
    
    def test_book_str_representation(self):
        gatsby = Book.objects.get(title='The Great Gatsby')
        kill_a_mockingbird = Book.objects.get(title='To Kill a Mockingbird')
        
        self.assertEqual(str(gatsby), 'The Great Gatsby by F. Scott Fitzgerald, published in 1925')
        self.assertEqual(repr(gatsby), 'The Great Gatsby by F. Scott Fitzgerald, published in 1925')
        
        self.assertEqual(str(kill_a_mockingbird), 'To Kill a Mockingbird by Harper Lee, published in 1960')
        self.assertEqual(repr(kill_a_mockingbird), 'To Kill a Mockingbird by Harper Lee, published in 1960')