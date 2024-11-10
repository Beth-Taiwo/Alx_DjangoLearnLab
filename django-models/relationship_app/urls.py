from django.urls import path
from .views import list_books,LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="Book list"),
    path("librarys/", LibraryDetailView.as_view(), name="Library Detail")
]