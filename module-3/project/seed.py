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


def seed():
    """Load sample data from sample_data.json and insert it into the database."""
    init_db()

    with open("sample_data.json") as f:
        data = json.load(f)

    # TODO: Loop through data["authors"] and call add_author() for each entry
    # TODO: Loop through data["books"] and call add_book() for each entry
    #       Tip: you'll need to look up author IDs to link them to books
    # TODO: Loop through data["members"] and call add_member() for each entry
    # TODO: Loop through data["borrowings"] and call checkout_book() for each entry
    #       Tip: look up book and member IDs by isbn / email
    # TODO: For borrowings that have a return_date, call return_book() to mark them returned

    print("Seed complete!")


if __name__ == "__main__":
    seed()