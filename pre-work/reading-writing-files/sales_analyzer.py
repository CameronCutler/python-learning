import csv
from collections import defaultdict

## Open file and read data into list of dicts ##
data = []
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        # Adding in revenue to the line items
        row["revenue"] = round((row["quantity"] * row["price"]), 2)
        data.append(row)
        
        
## Functions ## 
def get_total_revenue(numbers):
    # Generator expression way of doing it below
    # total_revenue = sum(item['revenue'] for item in numbers)
    
    total_revenue = 0
    for item in numbers:
        total_revenue = total_revenue + item["revenue"]
    
    return total_revenue

def get_revenue_per_product(data, product):
    revenue_per_product = 0 
    for item in data:
        if item["product"] == product:
            revenue_per_product = revenue_per_product + item["revenue"]
    return revenue_per_product


def get_quantity_per_product(data, product):
    quantity_per_product = 0
    for item in data:
        if item["product"] == product:
            quantity_per_product = quantity_per_product + item["quantity"]
    return quantity_per_product


def get_highest_revenue_day(data):
    category_totals = defaultdict(float)
    for item in data:
        category_totals[item["date"]] += item["revenue"]
    
    highest_revenue_day = max(category_totals, key=category_totals.get)
    return highest_revenue_day
        
##  Write to a sales report file ##
with open('sales_report.txt', 'w') as file:
    file.write("===== SALES REPORT =====\n\n")

    file.write(f"Widget A Total quantity => {get_quantity_per_product(data, "Widget A")}\n")
    file.write(f"Widget A Total Revenue => ${get_revenue_per_product(data, "Widget A")}\n")
    file.write(f"Widget B Total quantity => {get_quantity_per_product(data, "Widget B")}\n")
    file.write(f"Widget B Total Revenue => ${get_revenue_per_product(data, "Widget B")}\n")
    file.write(f"Widget C Total quantity => {get_quantity_per_product(data, "Widget C")}\n")
    file.write(f"Widget C Total Revenue => ${get_revenue_per_product(data, "Widget C")}\n\n")
    file.write(f"Highest Revenue Day => {get_highest_revenue_day(data)}\n\n")          
    file.write(f"Total Revenue => ${get_total_revenue(data)}\n")
print("Written to sales_report.txt")


# Write to csv
with open("product_summary.csv", "w", newline="") as file:
    products  = [{"product": "Widget A"}, {"product": "Widget B"}, {"product": "Widget C"}]
    writer = csv.DictWriter(file, fieldnames=["product","total_quantity", "total_revenue"])
    writer.writeheader()
    
    for product in products:
        product["total_quantity"] = get_quantity_per_product(data, product["product"])
        product["total_revenue"] = get_revenue_per_product(data, product["product"])
        
        writer.writerow(product)
print("Written to product_summary.csv")
