products = [
    {"name": "Laptop", "price": 999.99, "category": "electronics", "in_stock": True},
    {"name": "Python Book", "price": 39.99, "category": "books", "in_stock": True},
    {"name": "Headphones", "price": 149.99, "category": "electronics", "in_stock": False},
    {"name": "Desk Lamp", "price": 29.99, "category": "home", "in_stock": True},
    {"name": "AI Textbook", "price": 89.99, "category": "books", "in_stock": True},
    {"name": "Monitor", "price": 349.99, "category": "electronics", "in_stock": True},
    {"name": "Notebook", "price": 4.99, "category": "office", "in_stock": True},
    {"name": "Keyboard", "price": 79.99, "category": "electronics", "in_stock": False},
]

# Get all in-stock products (filter)
in_stock_products = [x for x in products if x["in_stock"] == True]
print(in_stock_products)


# Add a discounted_price field that is 10% off the original
discounted_products = [
    {**product, "discounted_price" : round(product["price"] * 0.9, 2)} for product in products
]
print(discounted_products)


# Get only electronics under $200
under_200_products = [product for product in products if product["category"] == "electronics" and product["price"] < 200.00]
print(under_200_products)


# Sort all products by price, lowest first (use sorted with a key lambda)
sorted_products = sorted(products, key=lambda product: product["price"])
print(sorted_products)


# Calculate the total value of all in-stock products (reduce or sum with comprehension)
total = sum(product["price"] for product in products)
print(total)


# Group products by category, return a dictionary like {"electronics": [...], "books": [...], ...}
grouped_by_category = {
    category: [product for product in products if product["category"] == category]
    for category in {product["category"] for product in products}
}
print(grouped_by_category)

import re
text = "Email alice@test.com or bob@work.org"
matches = re.findall(r'\b\w+@\w+\.\w+', text)
print(matches)