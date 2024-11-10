from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'books': books}
      return render(request, 'relationship_app/list_books.html', context)


# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.

class LibraryDetailView(DetailView):
      """Displays details for a specific library and lists all books available in that library."""
      model = Library
      template_name = 'relationship_app/library_detail.html'  # Template to use for rendering the view

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)  # Retrieve the context data from the superclass
            library = context['library']  # Get the library instance from the context
            context['books'] = library.books.all()  # Fetch all books associated with the library
            return context


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'