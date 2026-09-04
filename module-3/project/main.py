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
    title = input("Enter title: ")
    isbn = input("Enter ISBN: ")
    year = int(input("Enter year published: "))
    copies = int(input("Enter available copies: "))

    book = add_book(title, isbn, year, copies)
    print(f"Added book: {book.title}")


def handle_add_member():
    """Prompt for member details and register in the database."""
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    
    member = add_member(name, email)
    print(f"Added member: {member.name}")


def handle_search_books():
    """Prompt for a search term and display matching books."""
    keyword = input("Enter a title keyword: ").strip()
    books = search_books_by_title(keyword)

    if not books:
        print("No matching books found.")
        return

    for book in books:
        print(f"{book.id}: {book.title} | ISBN: {book.isbn} | Available: {book.available_copies}")


def handle_checkout():
    """Prompt for book ID and member ID, then check out the book."""
    books = list_books()
    if not books:
        print("No books available to check out.")
        return

    print("Available books:")
    for book in books:
        print(f"  {book.id}: {book.title} ({book.available_copies} available)")

    try:
        book_id = int(input("Enter book ID: ").strip())
        member_id = int(input("Enter member ID: ").strip())
        borrowing = checkout_book(book_id, member_id)
        print(f"Book checked out successfully. Borrowing ID: {borrowing.id}")
    except ValueError as exc:
        print(f"Error: {exc}")
    except Exception:
        print("Invalid input. Please enter numeric IDs.")


def handle_return():
    """Prompt for a borrowing ID and return the book."""
    try:
        borrowing_id = int(input("Enter borrowing ID: ").strip())
        borrowing = return_book(borrowing_id)
        print(f"Book returned successfully. Borrowing ID: {borrowing.id}")
    except ValueError as exc:
        print(f"Error: {exc}")
    except Exception:
        print("Invalid input. Please enter a numeric borrowing ID.")


def handle_member_borrowings():
    """Display all active borrowings for a member."""
    try:
        member_id = int(input("Enter member ID: ").strip())
        borrowings = list_member_borrowings(member_id)

        if not borrowings:
            print("No active borrowings for this member.")
            return

        for borrowing in borrowings:
            print(
                f"Borrowing ID {borrowing.id}: Book {borrowing.book_id} "
                f"checked out on {borrowing.checkout_date}"
            )
    except Exception:
        print("Invalid input. Please enter a numeric member ID.")


def handle_overdue():
    """Display all overdue borrowings."""
    overdue = list_overdue_books()

    if not overdue:
        print("No overdue books.")
        return

    for borrowing in overdue:
        print(
            f"Borrowing ID {borrowing.id}: Book {borrowing.book_id} "
            f"checked out on {borrowing.checkout_date}"
        )


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