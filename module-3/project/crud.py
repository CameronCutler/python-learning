"""
Module 3 Project: Library Management System
crud.py — Create, Read, Update, Delete operations

Your job: Implement every function below.
Import your models and engine from models.py.
"""

from models import engine, Book, Author, Member, Borrowing
from sqlalchemy.orm import Session
from datetime import date


# ──────────────────────────────────────────
# CREATE
# ──────────────────────────────────────────

def add_book(title: str, isbn: str, year_published: int = None,
             available_copies: int = 1):
    """Add a new book to the database. Returns the created Book object."""
    # TODO: open a Session, create a Book, add + commit, return it
    pass


def add_author(name: str, bio: str = None):
    """Add a new author. Returns the created Author object."""
    # TODO: implement
    pass


def add_member(name: str, email: str):
    """
    Register a new member with today's date as membership_date.
    Returns the created Member object.
    """
    # TODO: implement
    pass


def checkout_book(book_id: int, member_id: int):
    """
    Check out a book to a member.
    Decrements available_copies by 1 and sets checkout_date to today.
    Raises ValueError if available_copies == 0.
    Returns the created Borrowing object.
    """
    # TODO: implement
    pass


# ──────────────────────────────────────────
# READ
# ──────────────────────────────────────────

def list_books():
    """Return a list of all Book objects."""
    # TODO: implement
    pass


def search_books_by_title(title: str):
    """Return books whose title contains the given string (case-insensitive)."""
    # TODO: implement
    pass


def find_books_by_author(author_name: str):
    """Return all books associated with an author whose name contains author_name."""
    # TODO: implement
    pass


def list_member_borrowings(member_id: int):
    """Return all active (unreturned) Borrowing objects for the given member."""
    # TODO: implement
    pass


def list_overdue_books(days: int = 14):
    """
    Return Borrowing objects where return_date is NULL and
    checkout_date is more than `days` days ago.
    """
    # TODO: implement
    pass


# ──────────────────────────────────────────
# UPDATE
# ──────────────────────────────────────────

def return_book(borrowing_id: int):
    """
    Mark a borrowing as returned.
    Sets return_date to today and increments book.available_copies by 1.
    Raises ValueError if the borrowing is not found or already returned.
    """
    # TODO: implement
    pass


def update_member_email(member_id: int, new_email: str):
    """Update the email address for a member. Returns the updated Member object."""
    # TODO: implement
    pass


# ──────────────────────────────────────────
# DELETE
# ──────────────────────────────────────────

def delete_book(book_id: int):
    """
    Delete a book from the database.
    Raises ValueError if the book has any active (unreturned) borrowings.
    """
    # TODO: implement
    pass


def delete_member(member_id: int):
    """
    Delete a member from the database.
    Raises ValueError if the member has any active (unreturned) borrowings.
    """
    # TODO: implement
    pass