"""
Module 3 Project: Library Management System
models.py — SQLAlchemy models and database setup

Your job: Implement the models marked with # TODO.
All models must use SQLAlchemy 2.0 syntax: Mapped and mapped_column.
"""

from sqlalchemy import create_engine, String, Integer, ForeignKey, Table, Column, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from datetime import date

engine = create_engine("sqlite:///library.db", echo=False)


class Base(DeclarativeBase):
    pass


# Association table for Book <-> Author (many-to-many)
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id",   Integer, ForeignKey("books.id"),   primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
)


class Author(Base):
    """
    Represents an author in the library system.
    
    Attributes:
        id: Primary key identifier.
        name: Author's name (required).
        bio: Author's biography (optional).
        books: List of books authored by this author (many-to-many relationship).
    """
    __tablename__ = "authors"
   
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    bio: Mapped[str] = mapped_column(String(500), nullable=True)
    
    books: Mapped[list["Book"]] = relationship(
        back_populates="authors", 
        secondary=book_authors
    )
    
    def __repr__(self) -> str:
        return f"Author(id={self.id}, name='{self.name}')"


# Attributes: id (PK), name (required), email (unique, required), membership_date (date)
# Relationship: borrowings (one-to-many)
class Member(Base):
    """
    Represents a library member.

    Attributes:
        id: Primary key identifier.
        name: Member's full name (required).
        email: Unique email address for the member (required).
        membership_date: Date the member joined the library.
        borrowings: List of borrowing records for this member (one-to-many relationship).
    """
    __tablename__ = "members"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    membership_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)

    borrowings: Mapped[list["Borrowing"]] = relationship(
        back_populates="member",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Member(id={self.id}, name='{self.name}', email='{self.email}')"



# Attributes: id (PK), title (required), isbn (unique, required),
#             year_published (optional, integer), available_copies (integer, default 1)
# Relationships: authors (many-to-many via book_authors), borrowings (one-to-many)
class Book(Base):
    """
    Represents a book in the library inventory.

    Attributes:
        id: Primary key identifier.
        title: Book title (required).
        isbn: Unique ISBN number (required).
        year_published: Year the book was published (optional).
        available_copies: Number of copies currently available to borrow.
        authors: List of authors associated with this book (many-to-many).
        borrowings: List of borrowing records for this book (one-to-many).
    """
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    isbn: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    year_published: Mapped[int] = mapped_column(Integer, nullable=True)
    available_copies: Mapped[int] = mapped_column(Integer, default=1, nullable=False)

    authors: Mapped[list["Author"]] = relationship(
        back_populates="books",
        secondary=book_authors
    )
    borrowings: Mapped[list["Borrowing"]] = relationship(
        back_populates="book",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Book(id={self.id}, title='{self.title}', isbn='{self.isbn}')"


# Attributes: id (PK), book_id (FK -> books.id), member_id (FK -> members.id),
#             checkout_date (date), return_date (date, nullable — NULL means not yet returned)
# Relationships: book, member
class Borrowing(Base):
    """
    Represents a single book checkout by a member.

    Attributes:
        id: Primary key identifier.
        book_id: Foreign key to the borrowed book.
        member_id: Foreign key to the member who checked out the book.
        checkout_date: Date the book was checked out.
        return_date: Date the book was returned, or None if still outstanding.
        book: The book this borrowing references.
        member: The member this borrowing belongs to.
    """
    __tablename__ = "borrowings"

    id: Mapped[int] = mapped_column(primary_key=True)

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    member_id: Mapped[int] = mapped_column(ForeignKey("members.id"), nullable=False)

    checkout_date: Mapped[date] = mapped_column(Date, nullable=False, default=date.today)
    return_date: Mapped[date] = mapped_column(Date, nullable=True)

    book: Mapped["Book"] = relationship(back_populates="borrowings")
    member: Mapped["Member"] = relationship(back_populates="borrowings")

    def __repr__(self) -> str:
        return (
            f"Borrowing(id={self.id}, book_id={self.book_id}, "
            f"member_id={self.member_id}, checkout_date={self.checkout_date})"
        )


def init_db():
    """Create all tables in the database. Call once before using any other functions."""
    Base.metadata.create_all(engine)
    