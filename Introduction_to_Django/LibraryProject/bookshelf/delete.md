```bash
    >>> from bookshelf.models import Book

    # Retrieve all books from the database
    >>> Book.objects.all()
    # Expected Output: <QuerySet [Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949]>

    # Delete the book
    >>> Book.objects.all().delete
    # Expected Output: <bound method QuerySet.delete of <QuerySet [Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949]>>

    # assign book to variable book
    >>> book = Book.objects.get(title= ' Nineteen Eighty-Four')
    >>> book.delete()
    # Expected Output: (1, {'bookshelf.Book': 1})

    # Confirm deletion by retrieving all Book objects
    >>> Book.objects.all()
    # Expected Output: <QuerySet []>
```
