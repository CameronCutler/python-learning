import sqlite3
import pandas as pd


# Setup DB
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# columns: product, category, unit_price, quantity, quarter
cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        product TEXT NOT NULL,
        category TEXT NOT NULL,
        unit_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        quarter TEXT NOT NULL
    )
""")

sales_data = [
    ("Widget A", "Electronics", 29.99, 150, "2025-Q1"),
    ("Widget B", "Electronics", 49.99, 89, "2025-Q1"),
    ("Gadget X", "Accessories", 15.99, 300, "2025-Q1"),
    ("Widget A", "Electronics", 29.99, 200, "2025-Q2"),
    ("Gadget Y", "Accessories", 22.99, 175, "2025-Q2"),
    ("Widget C", "Electronics", 79.99, 50, "2025-Q2"),
    ("Gadget X", "Accessories", 15.99, 280, "2025-Q2"),
    ("Widget B", "Electronics", 49.99, 120, "2025-Q3"),
]

cursor.executemany(
    "INSERT INTO products (product, category, unit_price, quantity, quarter) VALUES (?, ?, ?, ?, ?)",
    sales_data
)
conn.commit()

# Load the same dataset into a pandas DataFrame
# Use the same column order as the database table
# (excluding the auto-increment id column)
df = pd.DataFrame(sales_data, columns=["product", "category", "unit_price", "quantity", "quarter"])

print("===Loaded in to pandas and SQL===")
print(df)
print()



# What is the total revenue (price × quantity) per product?
print("=== TOTAL REVENUE PER PRODUCT")
cursor.execute("""
      SELECT product,
      ROUND(SUM(unit_price * quantity), 2) AS total_revenue
      FROM products
      GROUP BY product
      ORDER BY total_revenue DESC  
""")

print("--- SQL ---")
for row in cursor.fetchall():
    print(f" {row[0]} - ${row[1]:,.2f}")
    

df["revenue"] = df["unit_price"] * df["quantity"]
revenue_by_product = (
    df.groupby("product", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

print("--- Pandas ---")
print(revenue_by_product)

# Which quarter had the highest total quantity sold?
print("\n=== QUARTER WITH HIGHEST TOTAL QUANTITY ===")

cursor.execute("""
    SELECT quarter, SUM(quantity) AS total_quantity
    FROM products
    GROUP BY quarter
    ORDER BY total_quantity DESC
    LIMIT 1
""")

print("--- SQL ---")
for row in cursor.fetchall():
    print(f" {row[0]} - {row[1]} units sold")

quarter_quantity = (
    df.groupby("quarter", as_index=False)["quantity"]
      .sum()
      .sort_values("quantity", ascending=False)
      .head(1)
)

print("--- Pandas ---")
print(quarter_quantity)

# What is the average unit price per category?
print("\n=== AVERAGE UNIT PRICE PER CATEGORY ===")

cursor.execute("""
    SELECT category,
           ROUND(AVG(unit_price), 2) AS avg_unit_price
    FROM products
    GROUP BY category
    ORDER BY avg_unit_price DESC
""")

print("--- SQL ---")
for row in cursor.fetchall():
    print(f" {row[0]} - ${row[1]:,.2f} average")

avg_price_by_category = (
    df.groupby("category", as_index=False)["unit_price"]
      .mean()
      .sort_values("unit_price", ascending=False)
)

print("--- Pandas ---")
print(avg_price_by_category)

# Which products had total quantity over 200 across all quarters?
print("\n=== PRODUCTS WITH TOTAL QUANTITY OVER 200 ===")

cursor.execute("""
    SELECT product,
           SUM(quantity) AS total_quantity
    FROM products
    GROUP BY product
    HAVING SUM(quantity) > 200
    ORDER BY total_quantity DESC
""")

print("--- SQL ---")
for row in cursor.fetchall():
    print(f" {row[0]} - {row[1]} units")

products_over_200 = (
    df.groupby("product", as_index=False)["quantity"]
      .sum()
      .query("quantity > 200")
      .sort_values("quantity", ascending=False)
)

print("--- Pandas ---")
print(products_over_200)