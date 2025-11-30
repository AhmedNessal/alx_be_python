class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title          # public attribute
        self.author = author        # public attribute
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if book is not checked out."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is
