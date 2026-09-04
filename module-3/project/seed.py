"""
Module 3 Project: Library Management System
seed.py — Populate the database with sample data for testing.

Run after implementing your models and CRUD functions:
    python seed.py

Sample data is loaded from sample_data.json.
"""

import json
from models import init_db
from crud import add_author, add_book, add_member, checkout_book, return_book
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import engine, Book, Author, Member
from datetime import datetime


def seed():
    """Load sample data from sample_data.json and insert it into the database."""
    init_db()

    with open("sample_data.json") as f:
        data = json.load(f)

    # TODO: Loop through data["authors"] and call add_author() for each entry
    for author in data["authors"]:
        add_author(
            name=author["name"], 
            bio=author["bio"]
        )
    # TODO: Loop through data["books"] and call add_book() for each entry
    #       Tip: you'll need to look up author IDs to link them to books
    for book in data["books"]:
        saved_book = add_book(
            title=book["title"], 
            isbn=book["isbn"], 
            year_published=book["year_published"],
            available_copies=book["available_copies"]
        )
        
        with Session(engine) as session:
            db_book = session.get(Book, saved_book.id)
            for author_name in book["authors"]:
                author = session.execute(
                    select(Author).where(Author.name == author_name)
                ).scalar_one()
                db_book.authors.append(author)
            session.commit()
            
    # TODO: Loop through data["members"] and call add_member() for each entry
    for member in data["members"]:
        add_member(
            name=member["name"],
            email=member["email"]
        )
        
    # TODO: Loop through data["borrowings"] and call checkout_book() for each entry
    #       Tip: look up book and member IDs by isbn / email
    for borrowing in data["borrowings"]:
        
        with Session(engine) as session:
            db_book = session.execute(
                select(Book).where(Book.isbn == borrowing["book_isbn"])
            ).scalar_one()
            db_member = session.execute(
                select(Member).where(Member.email == borrowing["member_email"])
            ).scalar_one()
            
            checkout_date = datetime.strptime(borrowing["checkout_date"], "%Y-%m-%d").date()
            return_date = (
                datetime.strptime(borrowing["return_date"], "%Y-%m-%d").date()
                if borrowing["return_date"] is not None
                else None
            )
            
            # Added checkout and return date to my checkout book function instead
            checked_out_book = checkout_book(
                db_book.id, 
                db_member.id, 
                checkout_date=checkout_date,
                return_date=return_date
            )

    print("Seed complete!")


if __name__ == "__main__":
    seed()