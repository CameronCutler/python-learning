# Convert prices and quantities to numbers before calculating each item subtotal.
item1_name = "Notebook"
item1_price = "4.99"
price1 = float(item1_price)
item1_qty = int("2")
item1_subtotal = price1 * item1_qty

item2_name = "Pen Pack"
item2_price = "7.50"
price2 = float(item2_price)
item2_qty = int("1")
item2_subtotal = price2 * item2_qty

item3_name = "Backpack"
item3_price = "34.99"
price3 = float(item3_price)
item3_qty = int("1")
item3_subtotal = price3 * item3_qty


# Add sales tax to the subtotal to get the amount due.
subtotal = item1_subtotal + item2_subtotal + item3_subtotal
tax_rate = float("0.075")
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount


# Print the receipt using the calculated amounts.
header_separator = "=" * 40
item_separator = "-" * 40

print(header_separator)
print("\t STORE RECEIPT")
print(header_separator)
print(f"{item1_name}\t ${price1:.2f} x {item1_qty} \t ${item1_subtotal:.2f}")
print(f"{item2_name}\t ${price2:.2f} x {item2_qty} \t ${item2_subtotal:.2f}")
print(f"{item3_name}\t ${price3:.2f} x {item3_qty} \t ${item3_subtotal:.2f}")
print(item_separator)
print(f"Subtotal: \t\t\t ${subtotal:.2f}")
print(f"Tax (7.5%): \t\t\t ${tax_amount:.2f}")
print(header_separator)
print(f"TOTAL: \t\t\t\t ${total:.2f}")
print(header_separator)