from django.urls import path
from .views import list_books,LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("books/", list_books, name="Book list"),
    path("librarys/", LibraryDetailView.as_view(), name="Library Detail"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register, name="Register"),
]