# Input
destination = input("What is your destination? ")
distance = int(input("What is the distance in miles? "))
fuel_efficiency = float(input("What is your fuel efficiency? "))
gas_price = float(input("What is the current gas price? "))
nights = int(input("How many nights? "))
avg_hotel_cost = float(input("Average hotel cost? "))
daily_food_budget = float(input("How much is budgeted for food each day? "))

# Calculate
total_gallons_gas = distance / fuel_efficiency
total_gas_cost = total_gallons_gas * gas_price
total_hotel_cost = nights * avg_hotel_cost
total_food_cost = (nights + 1) * daily_food_budget
total = total_gas_cost + total_hotel_cost + total_food_cost


# Total Width for Layout
w = 50

# Output Header
print("\n" + "=" * w)
print(f"{'Road Trip Budget Planner':^{w}}")
print("=" * w)
print(f"{'Destination:':<18} {destination}")
print(f"{'Distance:':<18} {distance} miles")
print(f"{'Number of nights:':<18} {nights}")

# Breakdown Table Header
print("\n" + "-" * w)
print(f"{'Category / Details':<35} {'Cost':>{w-36}}")
print("-" * w)

# Formatted Row Strings
gas_details = f"Gas ({total_gallons_gas:.1f} gal @ ${gas_price:.2f}/gal)"
hotel_details = f"Hotel ({nights} nights @ ${avg_hotel_cost:.2f}/nt)"
food_details = f"Food ({nights + 1} days @ ${daily_food_budget:.2f}/day)"

# Table Rows (Left-align details to 35 spaces, right-align costs to 15 spaces)
print(f"{gas_details:<35} {f'${total_gas_cost:.2f}':>15}")
print(f"{hotel_details:<35} {f'${total_hotel_cost:.2f}':>15}")
print(f"{food_details:<35} {f'${total_food_cost:.2f}':>15}")

# Totals Footer
print("-" * w)
print(f"{'ESTIMATED TOTAL:':<35} {f'${total:.2f}':>15}")
print("=" * w + "\n")