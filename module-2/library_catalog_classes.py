from typing import List

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
        if not self.checked_out:
            self.checked_out = True
        else:
            raise ValueError(f"{self.title} is already checked out!")
    
    def return_book(self) -> None:
        if self.checked_out == True:
            self.checked_out = False
        else:
            raise ValueError(f"{self.title} has not been checked out yet!")
        
    def __repr__(self): 
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year}, checked_out={self.checked_out})"

class EBook(Book):
    """A lightweight e-book representation that extends Book.

    Adds file size (in MB) and supports multiple simultaneous checkouts.
    """
    COPIES = 3
    def __init__(self, title: str, author: str, year: int, file_size_mb: float = 0,
                 checked_out_count: int = 0):
        super().__init__(title, author, year)
        if isinstance(file_size_mb, bool) or not isinstance(file_size_mb, (int, float)) or file_size_mb < 0:
            raise ValueError("file_size_mb must be a non-negative number")
        if isinstance(checked_out_count, bool) or not isinstance(checked_out_count, int):
            raise ValueError("checked_out_count must be an integer")
        if not 0 <= checked_out_count <= self.COPIES:
            raise ValueError(f"checked_out_count must be between 0 and {self.COPIES}")

        self.file_size_mb = float(file_size_mb)
        self.checked_out_count = checked_out_count
        self.copies = self.COPIES - checked_out_count
        self.checked_out = self.copies == 0
        
    def check_out(self) -> None:
        if self.copies == 0:
            raise ValueError(f"{self.title} is already checked out!")
        self.checked_out_count += 1
        self.copies -= 1
        self.checked_out = self.copies == 0
        
    def return_book(self) -> None:
        if self.checked_out_count == 0:
            raise ValueError(f"{self.title} has not been checked out yet!")
        self.checked_out_count -= 1
        self.copies += 1
        self.checked_out = False
        

    def __repr__(self):
        return (
            f"EBook(title={self.title!r}, author={self.author!r}, year={self.year}, size_mb={self.file_size_mb}, "
            f"checked_out={self.checked_out})"
        )
        
class Catalog:
    def __init__(self):
        self.books: List[Book] = []
        
    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self.books.append(book)
    
    def search_by_author(self, author: str) -> List[str]:
        if not isinstance(author, str):
            raise TypeError("search_by_author expects an author string")
        matching_titles = []
        search_author = author.lower()
        for book in self.books:
            if search_author in book.author.lower():
                matching_titles.append(book.title)
        return matching_titles
    
    def search_by_title(self, title: str) -> List[str]:
        if not isinstance(title, str):
            raise TypeError("search_by_title expects a title string")
        matching_titles = []
        search_title = title.lower()
        for book in self.books:
            if search_title in book.title.lower():
                matching_titles.append(book.title)
        return matching_titles

    def get_available(self) -> List[Book]:
        return [b for b in self.books if not b.checked_out]

    def summary(self) -> str:
        total_books = len(self.books)
        available_books = len(self.get_available())
        checked_out_books = total_books - available_books
        return (
            f"Total books: {total_books}\n"
            f"Available books: {available_books}\n"
            f"Checked out books: {checked_out_books}"
        )


if __name__ == "__main__":
    catalog = Catalog()
    catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
    catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
    catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

    results = catalog.search_by_title("e")
    print(results)

    author_results = catalog.search_by_author("n")
    print(author_results)

    # Check out
    catalog.books[0].check_out()
    available = catalog.get_available()
    print(f"Available: {len(available)} books")

    print(catalog.summary())