from django.urls import path, include
from .views import BookList, BookViewSet,AuthorView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('books/', BookList.as_view(), name="book-list"),
    path('', include(router.urls)),
    path('authors/', AuthorView.as_view(), name='author_view'),
]