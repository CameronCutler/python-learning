# Number 1
try:
    num1 = int(input("Enter the first number: "))
except ValueError:
    print("Invalid input. Setting value to 0.")
    num1 = 0

# Number 2
try:
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Setting value to 0.")
    num2 = 0

# Number 3
try:
    num3 = int(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Setting value to 0.")
    num3 = 0
 
 # Calculations
total_sum = num1 + num2 + num3
average = total_sum / 3.0

# Output results
print("\n--- Results ---")
print(f"Numbers entered: {num1}, {num2}, {num3}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")