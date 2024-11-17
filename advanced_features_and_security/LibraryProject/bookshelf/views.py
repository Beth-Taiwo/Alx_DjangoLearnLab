from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)


class LibraryDetailView(DetailView):
    """Displays details for a specific library and lists all books available in that library."""
    model = Library
    template_name = 'bookshelf/library_detail.html'  # Template to use for rendering the view

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Retrieve the context data from the superclass
        library = context['library']  # Get the library instance from the context
        context['books'] = library.books.all()  # Fetch all books associated with the library
        return context
    
    
class BookReviewView(DetailView, PermissionRequiredMixin):
    """
    Displays details for a specific book and its reviews.
    permission_required: The permission required to access this view.
    permission_required = 'bookshelf.review_book'
    """
    model = Book
    template_name = 'bookshelf/book_review.html'  # Template to use for rendering the view
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Retrieve the context data from the superclass
        book = context['book']  # Get the book instance from the context
        context['reviews'] = book.reviews.all()  # Fetch all reviews associated with the book
        return context