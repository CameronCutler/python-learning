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
# TODO: Define the book_authors association table
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id",   Integer, ForeignKey("books.id"),   primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.id"), primary_key=True),
)


# TODO: Implement the Author model
# Attributes: id (PK), name (required), bio (optional)
# Relationship: books (many-to-many via book_authors)
class Author(Base):
    __tablename__ = "authors"
    # TODO: define columns and relationship
    pass


# TODO: Implement the Member model
# Attributes: id (PK), name (required), email (unique, required), membership_date (date)
# Relationship: borrowings (one-to-many)
class Member(Base):
    __tablename__ = "members"
    # TODO: define columns and relationship
    pass


# TODO: Implement the Book model
# Attributes: id (PK), title (required), isbn (unique, required),
#             year_published (optional, integer), available_copies (integer, default 1)
# Relationships: authors (many-to-many via book_authors), borrowings (one-to-many)
class Book(Base):
    __tablename__ = "books"
    # TODO: define columns and relationships
    pass


# TODO: Implement the Borrowing model
# Attributes: id (PK), book_id (FK -> books.id), member_id (FK -> members.id),
#             checkout_date (date), return_date (date, nullable — NULL means not yet returned)
# Relationships: book, member
class Borrowing(Base):
    __tablename__ = "borrowings"
    # TODO: define columns and relationships
    pass


def init_db():
    """Create all tables in the database. Call once before using any other functions."""
    # TODO: Base.metadata.create_all(engine)
    pass