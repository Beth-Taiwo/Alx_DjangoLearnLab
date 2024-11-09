from relationship_app.models import Book,Library

# Query all books by a specific author.
books_by_author = Book.objects.filter(author__name="George Orwell")

for book in books_by_author:
    print(book.title)
    
library_name = Library.objects.create(name="Custodian")
    
# List all books in a library.
library = Library.objects.get(name=library_name)
books_in_library = library.books.all() 

for book in books_in_library:
    print(book.title)
    
# Retrieve the librarian for a library.
librarian = library.librarian
print(librarian.name)