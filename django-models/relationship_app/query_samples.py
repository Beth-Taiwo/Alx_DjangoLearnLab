from relationship_app.models import Author,Book,Library

author_name = Book.objects.create(name="George Orwell")

author = Author.objects.get(name=author_name)

# Query all books by a specific author.
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)
    
library_name = Library.objects.create(name="Custodian")
library_name.save()
    
# List all books in a library.
library = Library.objects.get(name=library_name)
books_in_library = library.books.all() 

for book in books_in_library:
    print(book.title)
    
# Retrieve the librarian for a library.
library = Library.objects.get(name=library_name)

librarian = Librarian.objects.get(library=library) # Access the related librarian via the OneToOne field
print(librarian.name)