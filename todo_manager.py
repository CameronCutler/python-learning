tasks = ["clean dishes", "wash laundry", "walk the dog"]

# Output
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
    
print(f"Total tasks: {len(tasks)}")

print("What would you like to do?")
print("1. Add a task")
print("2. Remove a task")

choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    new_task = input("What would you like to add to your list? ")
    tasks.append(new_task)
elif choice == "2":
    try:
        task_index = int(input("Which task would you like to remove? ")) - 1
    except ValueError:
        print("Invalid input: please enter a number.")
    else:
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
        else:
            print("Invalid task number: out of range.")

# Output updated list
print("\nUpdated Task List:")
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")
print(f"Total tasks: {len(tasks)}")