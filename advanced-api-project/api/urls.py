from django.urls import path, include
from .views import BookList, BookViewSet,AuthorView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('books/', BookList.as_view(), name="book-list"),
    path('', include(router.urls)),
    path('authors/', AuthorView.as_view(), name='author_view'),
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]