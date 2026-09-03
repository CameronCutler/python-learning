"""
Module 3 Project: Library Management System
main.py — Command-line interface

Your job: Implement each menu handler function below.
The main menu loop is already provided — just fill in the handlers.
"""

from models import init_db
from crud import (
    add_book, add_author, add_member, checkout_book, return_book,
    list_books, search_books_by_title, find_books_by_author,
    list_member_borrowings, list_overdue_books,
)


def handle_add_book():
    """Prompt for book details and add to the database."""
    # TODO: Use input() to collect title, isbn, year_published, available_copies
    # TODO: Call add_book() and print a confirmation message
    pass


def handle_add_member():
    """Prompt for member details and register in the database."""
    # TODO: Use input() to collect name and email
    # TODO: Call add_member() and print a confirmation message
    pass


def handle_search_books():
    """Prompt for a search term and display matching books."""
    # TODO: Prompt for a title keyword, call search_books_by_title(), print results
    pass


def handle_checkout():
    """Prompt for book ID and member ID, then check out the book."""
    # TODO: Show available books (call list_books())
    # TODO: Prompt for book_id and member_id
    # TODO: Call checkout_book() and handle ValueError (book not available)
    pass


def handle_return():
    """Prompt for a borrowing ID and return the book."""
    # TODO: Prompt for borrowing_id, call return_book(), print confirmation
    pass


def handle_member_borrowings():
    """Display all active borrowings for a member."""
    # TODO: Prompt for member_id, call list_member_borrowings(), print results
    pass


def handle_overdue():
    """Display all overdue borrowings."""
    # TODO: Call list_overdue_books() and print results
    pass


def main():
    init_db()

    while True:
        print("\n📚 Library Management System")
        print("1. Add a book")
        print("2. Add a member")
        print("3. Search books")
        print("4. Check out a book")
        print("5. Return a book")
        print("6. View member's borrowings")
        print("7. View overdue books")
        print("8. Exit")

        choice = input("\nChoose an option (1-8): ").strip()

        if choice == "1":
            handle_add_book()
        elif choice == "2":
            handle_add_member()
        elif choice == "3":
            handle_search_books()
        elif choice == "4":
            handle_checkout()
        elif choice == "5":
            handle_return()
        elif choice == "6":
            handle_member_borrowings()
        elif choice == "7":
            handle_overdue()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()