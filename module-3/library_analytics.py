import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Create tables
cursor.execute("""
    CREATE TABLE members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        join_date TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL,
        year_published INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE checkouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        checkout_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (member_id) REFERENCES members(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
""")

# Insert sample members
members = [
    (1, "Alice Johnson", "2023-01-15"),
    (2, "Ben Carter", "2022-08-11"),
    (3, "Cora Smith", "2024-02-04"),
    (4, "Daniel Lee", "2021-07-22"),
    (5, "Priya Patel", "2023-09-09"),
]

cursor.executemany(
    "INSERT INTO members (id, name, join_date) VALUES (?, ?, ?)",
    members,
)

# Insert sample books across multiple genres
books = [
    (1, "The Hobbit", "Fantasy", 1937),
    (2, "Pride and Prejudice", "Classic", 1813),
    (3, "The Martian", "Science Fiction", 2011),
    (4, "Atomic Habits", "Self-Help", 2018),
    (5, "The Silent Patient", "Mystery", 2019),
    (6, "Educated", "Memoir", 2018),
    (7, "Circe", "Fantasy", 2018),
    (8, "The Very Hungry Caterpillar", "Children", 1969),
]

cursor.executemany(
    "INSERT INTO books (id, title, genre, year_published) VALUES (?, ?, ?, ?)",
    books,
)

# Insert sample checkouts (18 total)
checkouts = [
    (1, 1, 1, "2024-01-05", "2024-01-12"),
    (2, 1, 3, "2024-02-03", "2024-02-14"),
    (3, 2, 5, "2024-02-10", "2024-02-18"),
    (4, 2, 2, "2024-03-01", None),
    (5, 3, 1, "2024-03-07", None),
    (6, 3, 7, "2024-03-19", "2024-03-27"),
    (7, 3, 6, "2024-03-21", "2024-04-02"),
    (8, 4, 4, "2024-04-04", "2024-04-11"),
    (9, 4, 7, "2024-04-15", "2024-04-22"),
    (10, 4, 2, "2024-05-01", None),
    (11, 5, 3, "2024-05-10", "2024-05-18"),
    (12, 5, 5, "2024-05-12", None),
    (13, 1, 7, "2024-05-20", "2024-05-30"),
    (14, 2, 4, "2024-06-02", None),
    (15, 3, 2, "2024-06-10", "2024-06-16"),
    (16, 5, 1, "2024-06-15", "2024-06-22"),
    (17, 1, 6, "2024-06-20", None),
    (18, 2, 1, "2024-06-28", None),
]

cursor.executemany(
    """
    INSERT INTO checkouts (id, member_id, book_id, checkout_date, return_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    checkouts,
)

connection.commit()

# 1. How many books are in each genre?
print("\n=== Books per genre ===")
cursor.execute("""
    SELECT genre, COUNT(*) AS book_count
    FROM books
    GROUP BY genre
    ORDER BY genre
""")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")

# 2. Which member has checked out the most books?
print("\n=== Most active member ===")
cursor.execute("""
    SELECT m.name, COUNT(c.id) AS checkout_count
    FROM members m
    JOIN checkouts c ON m.id = c.member_id
    GROUP BY m.id, m.name
    ORDER BY checkout_count DESC, m.name ASC
    LIMIT 1
""")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]} checkouts")

# 3. Average number of checkouts per member
print("\n=== Average checkouts per member ===")
cursor.execute("""
    SELECT AVG(checkout_count) AS average_checkouts_per_member
    FROM (
        SELECT COUNT(*) AS checkout_count
        FROM checkouts
        GROUP BY member_id
    )
""")
for row in cursor.fetchall():
    print(f"{row[0]:.2f}")

# 4. Which genres have more than 3 checkouts?
print("\n=== Genres with more than 3 checkouts ===")
cursor.execute("""
    SELECT b.genre, COUNT(c.id) AS checkout_count
    FROM checkouts c
    JOIN books b ON c.book_id = b.id
    GROUP BY b.genre
    HAVING COUNT(c.id) > 3
    ORDER BY checkout_count DESC, b.genre ASC
""")
for row in cursor.fetchall():
    print(f"{row[0]}: {row[1]}")

# 5. Which books have never been checked out?
print("\n=== Books never checked out ===")
cursor.execute("""
    SELECT title
    FROM books
    WHERE id NOT IN (
        SELECT DISTINCT book_id
        FROM checkouts
    )
    ORDER BY title
""")
for row in cursor.fetchall():
    print(row[0])

connection.close()
