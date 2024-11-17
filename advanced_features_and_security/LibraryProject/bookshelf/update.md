```bash
    >>> from bookshelf.models import Book

    # Retrieving the book instance with the title "1984"
    >>> book = Book.objects.get(title='1984')

    # Checking the current details of the book
    >>> book
    # Expected Output: Title: 1984, Author: George Orwell, Year: 1949

    # Updating the title of the book to "Nineteen Eighty-Four" and saving changes
    >>> book.title = "Nineteen Eighty-Four"
    >>> book.save()


    # Checking that the title was updated
    >>> book.title
    # Expected Output: 'Nineteen Eighty-Four'


    >>> Book.objects.all()
    # Expected Output: <QuerySet [Title: Nineteen Eighty-Four, Author: George Orwell, Year: 1949]>
```
