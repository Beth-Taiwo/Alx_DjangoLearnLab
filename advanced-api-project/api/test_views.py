from django.test import TestCase
from .models import Book, Author
from rest_framework.test import APITestCase
# from .views import BookViewSet
from rest_framework import status

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
        
        

class BookViewSetTestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='F. Scott Fitzgerald')
        
    def test_create_book(self):
        """
        Ensure we can create a new book
        """
        url = '/api/books_all/'
        data = {
            'title': 'F. Scott Fitzgerald',
            'author': self.author.pk,
            'publication_year': 1949,
        }
        response =  self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'F. Scott Fitzgerald')
        
        
    def test_get_books(self):
        """
        Ensure we can retrieve a list of books
        """
        Book.objects.create(title='The Great Gatsby', author=self.author, publication_year=1925)
        Book.objects.create(title='To Kill a Mockingbird', author=self.author, publication_year=1960)
        
        url = '/api/books_all/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')
        self.assertEqual(response.data[1]['title'], 'To Kill a Mockingbird')
        
        
class AuthorTestCase(APITestCase):
    def test_create_author(self):
        """
        Ensure we can create a new author
        """
        url = '/api/authors_all/'
        data = {'name': 'F. Scott Fitzgerald'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, 'F. Scott Fitzgerald')