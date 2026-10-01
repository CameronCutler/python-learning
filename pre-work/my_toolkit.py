def calculate_average(numbers):
    """Return the rounded average of a list of numbers, or 0 if it is empty."""
    if not numbers:
        return 0
    elif isinstance(numbers, list):
        return round(sum(numbers)/len(numbers), 2)
    else:
        print("Numbers are not in a list")
        return None
    
def find_max_and_min(numbers):
    """Return the maximum and minimum values from a non-empty iterable.

    Raises ValueError if numbers is empty.
    """
    try:
        first_number = numbers[0]
    except IndexError:
        raise ValueError("numbers must not be empty") from None

    maximum = minimum = first_number
    for number in numbers:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number

    return maximum, minimum


def count_occurrences(numbers, target):
    """Count how many times target appears in numbers."""
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

def is_palindrome(text):
    """Return whether text reads the same backward after lowercasing and removing spaces."""
    cleaned = text.lower().replace(" ", "")
    reverse = cleaned[::-1]
    if reverse == cleaned:
        return True
    else:
        return False

def create_report(text, numbers):
    """Build a report containing text, the average, and the maximum/minimum values."""
    return f"{text} => Average score: {calculate_average(numbers)}, Max and Min scores: {find_max_and_min(numbers)}"
    
if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93, -25, 0, 110, 85]
    empty_scores = []
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print(f"'A man a plan a canal Panama' palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print()
    print(create_report("Class Scores", test_scores))
    # print(create_report("Empty Scores", empty_scores))
