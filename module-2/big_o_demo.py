import time
import random

def has_duplicate_slow(data):
    """Compare every element to every other element.

    Args:
        data (_type_): _description_
    """
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] == data[j]:
                return True
    return False

def has_duplicate_fast(data):
    # Use a set - seen items are tracked for instant lookup.
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False
    

def benchmark(func, data):
    """Time how long a function takes."""
    start = time.time()
    func(data)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000, 20000, 50000]

for size in sizes:
    data = list(range(size))
    random.shuffle(data)
    
    slow_time = benchmark(has_duplicate_slow, data)
    fast_time = benchmark(has_duplicate_fast, data)
    
    print(f"n={size:>6}     |   Slow: {slow_time:.4f}s  |   Fast: {fast_time:.4f}s")