from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="Book list"),
    path("librarys/", views.LibraryDetailView.as_view(), name="Library Detail")
]