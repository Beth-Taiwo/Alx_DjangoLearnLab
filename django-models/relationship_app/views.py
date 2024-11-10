from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book, UserProfile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

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
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    

@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Admin')
def admin_view(request):
      """Displays a view for administrative purposes."""
      # Code to handle admin view goes here
      return render(request, 'relationship_app/admin_view.html')


@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Librarian')
def librarian_view(request):
      """Displays a view for librarian purposes."""
      # Code to handle librarian view goes here
      return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Member')
def member_view(request):
      """Displays a view for member purposes."""
      # Code to handle member view goes here
      return render(request, 'relationship_app/member_view.html')
