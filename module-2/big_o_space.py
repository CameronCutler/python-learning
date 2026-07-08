# Function A
# O(N) space complexity because it grows with the size of the string
def reverse_string(s):
    return s[::-1]

# Function B
# O(1) since it has a limit on dict length to only the number of unique characters 
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Function C
# O(N^2) the memory grows proportional to the number of matrix entries
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Function D
# O(1) since it only has the one variable, total, it is a fixed space in memory
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)


# Part 2

# Loads emails into a set
def find_duplicate_email_addresses_fast(data):
    seen = set()
    duplicates = set()
    for address in data:
        if address in seen:
            duplicates.add(address)
        else:
            seen.add(address)
    return duplicates

# Sorts the file and scans for adjacent duplicates
# This function takes a long time since it sorting the data, then looping through it, but it has O(1) space complexity and O(n log n) time complexity
def find_duplicate_email_addresses_slow(data):
    duplicates = set()
    data.sort()
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            duplicates.add(data[i])
    return duplicates