def calculate_average(numbers):
    if not numbers:
        return 0
    elif isinstance(numbers, list):
        return round(sum(numbers)/len(numbers), 2)
    else:
        print("Numbers are not in a list")
        return None
    
def find_max_and_min(numbers):
    max, min = 0, 100
    for number in numbers:
        if number > max:
            max = number
        elif number < min:
            min = number
            
    return (max,min)


def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    reverse = cleaned[::-1]
    if reverse == cleaned:
        return True
    else:
        return False

def create_report(text, numbers):
        return f"{text} => Average score: {calculate_average(numbers)}, Max and Min scores: {find_max_and_min(numbers)}"
    
if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))
