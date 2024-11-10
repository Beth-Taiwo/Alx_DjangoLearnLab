from django.urls import path
from .views import list_books,LibraryDetailView
from .views import list_books,LibraryDetailView,admin_view,librarian_view,member_view
from . import views


urlpatterns = [
    path("books/", list_books, name="Book list"),
    path("librarys/", LibraryDetailView.as_view(), name="Library Detail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name="Register"),
    path('admin_view/', admin_view, name="Admin view"),
    path('librarian_view/', librarian_view, name="Librarian view"),
    path('member_view/', member_view, name="Member view"),
]