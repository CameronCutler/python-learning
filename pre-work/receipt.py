item1_name = "Notebook"
item1_price = float("4.99")
item1_qty = int("2")
item1_subtotal = item1_price * item1_qty

item2_name = "Pen Pack"
item2_price = float("7.50")
item2_qty = int("1")
item2_subtotal = item2_price * item2_qty

item3_name = "Backpack"
item3_price = float("34.99")
item3_qty = int("1")
item3_subtotal = item3_price * item3_qty

subtotal = item1_subtotal + item2_subtotal + item3_subtotal

tax_rate = float("0.075")


print("=" * 40)
print("\t STORE RECEIPT")
print("=" * 40)
print(f"{item1_name}\t ${item1_price} x {item1_qty} \t ${item1_subtotal:.2f}")
print(f"{item2_name}\t ${item2_price:.2f} x {item2_qty} \t ${item2_subtotal:.2f}")
print(f"{item3_name}\t ${item3_price} x {item3_qty} \t ${item3_subtotal:.2f}")
print("-" * 40)
print(f"Subtotal: \t\t\t ${subtotal}")
print(f"Tax (7.5%): \t\t\t ${subtotal * tax_rate:.2f}")
print("=" * 40)
print(f"TOTAL: \t\t\t\t ${subtotal * tax_rate + subtotal:.2f}")
print("=" * 40)