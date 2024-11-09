```bash
    >>> from bookshelf.models import Book
    # Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
    >>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949 )
    # Expected Output: Title: 1984, Author: George Orwell, Year: 1949

    # Retrieve
    >>> book.objects.get().title
    # Expected Output: '1984'

    >>> book.objects.get().author
    # Expected Output: 'George Orwell'

    >>> book.objects.get().publication_year
    # Expected Output: 1949

    # Update
    # Updating the title of the book to "Nineteen Eighty-Four" and saving changes
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()

    # Delete
    >>> book = Book.objects.get(title= ' Nineteen Eighty-Four')
    >>> book.delete()
    # Expected Output: (1, {'bookshelf.Book': 1})

    # Confirm deletion by retrieving all Book objects
    >>> book.objects.all()
    # Expected Output: <QuerySet []>
```
