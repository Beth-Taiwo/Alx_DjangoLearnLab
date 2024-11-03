```bash
    >>> from bookshelf.models import Book
    # Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
    >>> book = Book(title="1984", author="George Orwell", publication_year=1949 )

    # Save the object into the database. You have to call save() explicitly.
    >>> book.save()
```
