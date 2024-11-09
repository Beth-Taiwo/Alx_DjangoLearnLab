```bash
    >>> from bookshelf.models import Book

    >>> Book.objects.get().title
    # Expected Output: '1984'

    >>> Book.objects.get().author
    # Expected Output: 'George Orwell'

    >>> Book.objects.get().publication_year
    # Expected Output: 1949
```
