from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="Book list"),
    path("librarys/", views.LibraryDetailView.as_view(), name="Library Detail")
]