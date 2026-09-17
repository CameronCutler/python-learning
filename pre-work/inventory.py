inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 79.99, "quantity": 30},
    "monitor": {"price": 249.99, "quantity": 20},
    "headphones": {"price": 59.99, "quantity": 40},
}

# Display the full inventory
print(f"{'Item':<15}{'Price':>10}{'Quantity':>12}")
print("-" * 37)
for item, details in inventory.items():
    print(f"{item:<15}${details['price']:>9.2f}{details['quantity']:>12}")


# Calculate and display the total inventory value
total_value = 0
for details in inventory.values():
    total_value += details['price'] * details['quantity']
print(f"\nTotal inventory value: ${total_value:.2f}")

# Look up a product safely
product_name = input("\nEnter a product name to look up: ").strip().lower()
product = inventory.get(product_name)

if product is None:
    print(f"{product_name} was not found in the inventory.")
else:
    print(f"Product: {product_name}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Quantity: {product['quantity']}")


# Update the quantity of a product
update_product_name = input("\nEnter a product name to update: ").strip().lower()
if update_product_name in inventory:
    new_quantity = int(input(f"Enter the new quantity for {update_product_name}: "))
    inventory[update_product_name]['quantity'] = new_quantity
    print(f"Updated {update_product_name} quantity to {new_quantity}.")
else:
    print(f"{update_product_name} was not found in the inventory.")

# Track products with fewer than 10 items in stock
low_stock_products = set()
for item_name, details in inventory.items():
    if details['quantity'] < 10:
        low_stock_products.add(item_name)

print(f"\nLow-stock products: {low_stock_products}")