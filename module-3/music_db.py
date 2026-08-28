import sqlite3

# This creates a new database file called bookstore.db
# If the file already exists, it connects to it
connection = sqlite3.connect("music.db")

# A cursor is what you use to execute SQL commands
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# create artists table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        genre TEXT
    )
""")

# create albums table with artist_id foreign key
cursor.execute("""
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        artist_id INTEGER NOT NULL,
        FOREIGN KEY (artist_id) REFERENCES artists(id)
    )
""")

connection.commit()
print("Tables created!")


# Insert artists 
artists = [
    ("Sheryl Crowe", "Country"),
    ("Blink-182", "Rock"),
    ("Green Day", "Rock"),
    ("Kendrick Lamar", "Hip-Hop"),
    ("PawPaw Rod", "Soul")
]

cursor.executemany("""
    INSERT INTO artists (name, genre) VALUES (?, ?)
""", artists)
connection.commit()
print("Artists Inserted!")


# Insert Albums by artists
albums = [
    ["Picture Day", 2026, 5],
    ["The Blacker the Berry", 2015, 4],
    ["DAMN", 2017, 4],
    ["American Idiot", 2004, 3],
    ["Dookie", 1994, 3],
]
cursor.executemany("""
    INSERT INTO albums (title, year, artist_id) VALUES (?, ?, ?)
""", albums)
connection.commit()
print("Albums inserted!")


query = """
    SELECT a.title, a.year, ar.genre, ar.name
    FROM albums AS a
    JOIN artists AS ar
        ON a.artist_id = ar.id
    ORDER BY a.title
"""

rows = cursor.execute(query).fetchall()

for title, year, genre, artist_name in rows:
    print(f"{genre} Album '{title}' ({year}) belongs to {artist_name}.")