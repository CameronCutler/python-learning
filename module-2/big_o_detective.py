import time
import random

# Function A
# O(1) as it is getting data in a list. Simple
def get_first(data):
    return data[0]

# Function B
# O(N) as it is looping through the list once
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count

# Function C
# O(N^2) as it has a loop within a loop
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs

# Function D
# This function returns the number of halvings needed to reduce the number to 0. Because the loop is getting smaller with each go round it is O(log(N)) complexity
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# Function E
# This function uses 3 different complexities. line 1 O(n), line 2 O(n log n), line 3 O(1). We go with the longest one for the result which is O(n log n)
def process(data):
    total = sum(data)           # Line 1
    sorted_data = sorted(data)  # Line 2
    first = data[0]             # Line 3
    return total, sorted_data, first

def count_pairs_slow(data, target_sum):
    count = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[j] + data[i] == target_sum:
                count += 1
    return count

def count_pairs_fast(data, target_sum):
    count = 0
    seen = set()
    # Loop through the data once
    for value in data:
        # Find the complement to a given number by subratcting
        complement = target_sum - value
        # If the complement is in the set, then we know that we can increment the count
        if complement in seen:
            count += 1
        seen.add(value)
        
    return count

def benchmark(func, data, target):
    """Time how long a function takes."""
    start = time.time()
    func(data, target)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000, 20000]

for size in sizes:
    data = list(range(size))
    random.shuffle(data)
    
    slow_time = benchmark(count_pairs_slow, data, 45)
    fast_time = benchmark(count_pairs_fast, data, 45)
    
    print(f"n={size:>6}     |   Slow: {slow_time:.4f}s  |   Fast: {fast_time:.4f}s")