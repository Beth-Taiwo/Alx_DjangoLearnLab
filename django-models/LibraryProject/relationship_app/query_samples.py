from relationship_app.models import Book,Library

# Query all books by a specific author.
books_by_author = Book.objects.filter(author__name="George Orwell")

for book in books_by_author:
    print(book.title)
    
# List all books in a library.
books_in_library = Library.objects.get(name="Custodian")

for book in books_in_library:
    print(book.title)
    
# Retrieve the librarian for a library.
librarian = library.librarian
print(librarian.name)