from .serializers import BookSerializer, AuthorSerializer
from.models import Book, Author
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

# Create your views here.

# A nested BookSerializer to serialize the related books dynamically.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Implement a set of generic views for the Book model to handle CRUD operations. This includes:

# A ListView for retrieving all books.
# A DetailView for retrieving a single book by ID.
# A CreateView for adding a new book.
# An UpdateView for modifying an existing book.
# A DeleteView for removing a book.


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    

class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books/'
    

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    

# Implement a set of generic views for the Author model to handle CRUD operations. This includes:


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'
    

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    success_url = '/authors/'
    

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/authors/'
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    
