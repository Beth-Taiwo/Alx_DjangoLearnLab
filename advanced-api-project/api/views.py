from .serializer import BookSerializer, AuthorSerializer
from.models import Book, Author
from rest_framework import generics, viewsets
from rest_framework.response import Response

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


   