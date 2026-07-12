from collections import deque

class Node:
    "Single node in a linked list"
    def __init__(self, value):
        self. value = value
        self.next= None
    
    def __repr__(self):
        return f"Node ({self.value})"
    
class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None  # The list starts empty

    def insert_at_beginning(self, value):
        """Add a new node at the front of the list. O(1) time."""
        new_node = Node(value)
        new_node.next = self.head  # New node points to the old head
        self.head = new_node       # New node becomes the new head

    def insert_at_end(self, value):
        """Add a new node at the end of the list. O(n) time — must traverse to the end."""
        new_node = Node(value)
        if self.head is None:      # List is empty
            self.head = new_node
            return
        current = self.head
        while current.next:        # Walk to the last node
            current = current.next
        current.next = new_node    # Last node now points to the new node

    def search(self, target):
        """Find a value in the list. Returns True/False. O(n) time."""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next  # Follow the pointer to the next node
        return False

    def display(self):
        """Print the list in a readable format."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")
        
    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        current = self.head
        previous = None
        while current:
            if current.value == target:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next  # Follow the pointer to the next node
        return False

    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next        
        return count

    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        current = self.head
        converted_list = []
        while current:
            converted_list.append(current.value)
            current = current.next
        return converted_list
            
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
print(ll.length())     # 5
ll.delete(30)
ll.display()           # 10 -> 20 -> 40 -> 50 -> None
print(ll.to_list())    # [10, 20, 40, 50]



# Part 2 Bracket Validator
# Write a function that checks whether a string of brackets is properly balanced using a stack:

def is_balanced(text):
    """Return True if all brackets in text are properly matched.
    Handles: (), [], {}
    """
    stack = []
    matching = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in text:
        # If character is an open bracket, add it to the stack
        if char in "([{":
            stack.append(char)
        # if character is a close bracket 
        elif char in matching:
            # If nothing in the stack or the stack doesn't match the closing character, then return false
            if not stack or stack[-1] != matching[char]:
                return False
            # If it does match, pop it off the stack
            stack.pop()
    # If the stack is empty at the end of the string, yay! return true
    return len(stack) == 0

# Tests:
print(is_balanced("()"))           # True
print(is_balanced("({[]})"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("hello (world)")) # False



# Part 3 Task processor and queues

class TaskProcessor:
    def __init__(self):
        self.queue = deque()
    
    def add_task(self, name):
        self.queue.append(name)
    
    def process_next(self):
        # Should return the oldest unprocessed task or None if empty
        if self.queue:
            return self.queue.popleft()
        return None
     