from typing import List, Iterable, Optional

class Book:
    def __init__(self, title: str, author: str, year: int, checked_out: bool = False ):
        self.title = title
        self.author = author
        # validate year: must be an int and positive
        if not isinstance(year, int):
            raise ValueError(f"year must be an int, got {type(year).__name__}")
        if year <= 0:
            raise ValueError("year must be a positive integer")
        self.year = year
        self.checked_out = checked_out
        
    def check_out(self) -> None:
        if self.checked_out == False:
            self.checked_out = True
        else:
            raise Exception(f"{self.title} is already checked out!")
    
    def return_book(self) -> None:
        if self.checked_out == True:
            self.checked_out = False
        else:
            raise Exception(f"{self.title} has not been checked out yet!")
        
    def __repr__(self): 
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year}, checked_out={self.checked_out})"

class EBook(Book):
    """A lightweight e-book representation that extends Book.

    Adds file format and file size (in KB). Validates inputs and reuses
    the checkout behavior from the base class.
    """
    COPIES = 3
    def __init__(self, title: str, author: str, year: int, file_size_mb: float = 0,
                 checked_out: bool = False):
        super().__init__(title, author, year, checked_out)
        self.copies = self.COPIES
        if not isinstance(file_size_mb, float) or file_size_mb < 0:
            raise ValueError("file_size_mb must be a non-negative float")

        self.file_size_mb = file_size_mb
        
    def check_out(self) -> None:
        if self.checked_out == False and self.copies > 0:
            self.checked_out = True
            self.copies -= 1
        else:
            raise Exception(f"{self.title} is already checked out!") 

    def __repr__(self):
        return (
            f"EBook(title={self.title!r}, author={self.author!r}, year={self.year}, size_kb={self.file_size_mb}, "
            f"checked_out={self.checked_out})"
        )
        
class Catalog:
    def __init__(self):
        self.books: List[Book] = []
        
    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self.books.append(book)
    
    def search_by_author(self, author: str) -> str:
        if not isinstance(author, str):
            raise TypeError("search_by_author expects an author string")
        for book in self.books:
            if author in book.author.lower():
                return book.title
    
    def search_by_title(self, title: str) -> str:
        if not isinstance(title, str):
            raise TypeError("search_by_title expects a title string")
        for book in self.books:
            if title in book.title.lower():
                return book.title

    def get_available(self) -> List[Book]:
        return [b for b in self.books if not b.checked_out]


#  Testing Code 
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")