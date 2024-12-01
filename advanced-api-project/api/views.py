from .serializers import BookSerializer, AuthorSerializer
from.models import Book, Author
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import filters

# Create your views here.

# A nested BookSerializer to serialize the related books dynamically.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'author','publication_year']
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title', 'author','publication_year']
    ordering_fields = ['title', 'publication_year']
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
   

class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Implement a set of generic views for the Book model to handle CRUD operations. This includes:

# A CreateView for adding a new book.
# An UpdateView for modifying an existing book.
# A DeleteView for removing a book.
# A DetailView for retrieving a single book by ID.
# A ListView for retrieving all books.


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    # success_url = '/books/'
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Book created successfully'})
    

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Book updated successfully'})
    

class BookDeleteView(DeleteView):
    model = Book
    # success_url = '/books/'
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        return Response({'message': 'Book deleted successfully'})
    

class BookDetailView(DetailView):
    model = Book
    # template_name = 'books/book_detail.html'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        return Response({'message': 'Book details retrieved successfully'})
    
    
class BookListView(ListView):
    model = Book
    # template_name = 'books/book_list.html'
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title', 'author','publication_year']
    ordering_fields = ['title', 'publication_year']
    
    def get(self, request):
        return Response({'message': 'Book list retrieved successfully'})
    

# Implement a set of generic views for the Author model to handle CRUD operations. This includes:


class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'
    # success_url = '/authors/'
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Author created successfully'})    
    

class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    # success_url = '/authors/'
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Author updated successfully'})
    

class AuthorDeleteView(DeleteView):
    model = Author
    # success_url = '/authors/'
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message': 'Author deleted successfully'})
    

class AuthorDetailView(DetailView):
    model = Author
    # template_name = 'authors/author_detail.html'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        return Response({'message': 'Author details retrieved successfully'})
    
