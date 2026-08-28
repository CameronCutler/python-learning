import sqlite3

# This creates a new database file called bookstore.db
# If the file already exists, it connects to it
connection = sqlite3.connect("bookstore.db")

# A cursor is what you use to execute SQL commands
cursor = connection.cursor()

print("Connected to database!")

# Create a customers table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

connection.commit()

print("Customers table created!")


# Insert some data
cursor.execute("""
    INSERT INTO customers (name, email) 
    VALUES ('Maria Santos', 'maria@email.com')
""")
cursor.execute("""
    INSERT INTO customers (name, email) 
    VALUES ('James Chen', 'james@email.com')
""")

# Insert multiple customers at once
more_customers = [
    ("Aisha Johnson", "aisha@email.com"),
    ("David Kim", "david@email.com"),
]
cursor.executemany("""
    INSERT INTO customers (name, email) VALUES (?, ?)
""", more_customers)

connection.commit()
print("Customers inserted!")

# Read the data back
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()

print("\nAll customers:")
for row in rows:
    print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    
connection.close()
print("\nConnection closed.")