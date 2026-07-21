import pandas as pd
import matplotlib.pyplot as plt

messy = pd.DataFrame({
    "product": ["Widget A", "Widget B", "widget a", "Widget C", "Widget B",
                "Widget A", " Widget C", "Widget D", None, "Widget A"],
    "sales": ["150", "200", "175", "300", "200",
              "180", "250", "abc", "100", "-50"],
    "date": ["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03",
             "2025-01-03", "2025-01-04", "2025-01-04", "2025-01-05", "2025-01-05"],
    "region": ["North", "South", "north", "East", "South",
               "West", "east", "North", "South", "West"],
})

# print(messy.shape)
# 10,4
# print(messy.dtypes)
# str
# print(messy.duplicated().sum())
# 0

# Remove whitespace in str & capitalize
messy["product"] = messy["product"].str.strip().str.title()
messy["region"] = messy["region"].str.strip().str.title()


# Convert to numbers and dates and add NAN
messy["sales"] = pd.to_numeric(messy["sales"], errors="coerce")
messy["date"] = pd.to_datetime(messy["date"], errors="coerce")

# Remove impossible numbers
messy.loc[messy["sales"] < 0, "sales"] = pd.NA

# Drop NAN
clean = messy.dropna()

print(clean)

# Use matplotlib to generate a bar graph of total sales by product
sales_by_product = clean.groupby("product")["sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sales_by_product.plot(kind="bar", color="steelblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_by_product.png")
plt.show()

# Daily sales trend
daily_sales = clean.groupby("date")["sales"].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot(kind="line", color="coral", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_sales_trend.png")
plt.show()


# Distribution
plt.figure(figsize=(10, 6))
clean["sales"].plot(kind="hist", bins=8, color="red", edgecolor="black")
plt.title("Sales Distribution")
plt.xlabel("Frequency")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()