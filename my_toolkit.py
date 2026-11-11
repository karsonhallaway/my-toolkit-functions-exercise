def calculate_average(numbers):
    """Takes a list of numbers, returns the average. Returns 0 if the list is empty."""
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
    

def find_max_and_min(numbers):
    """Takes a list of numbers, returns a tuple (max_value, min_value) DO NOT USE max() and min() built in functions."""
    if not numbers:
        return (0, 0)
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return (max_value, min_value)
    
def count_occurrences(items, target):
    """Takes a list and a target value, returns how many times the target appears in the list. DO NOT USE .count() method."""
    if not items:
        return 0
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
    
def is_palindrome(text):
    """Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces.)"""
    cleaned_text = text.replace(" ", "").lower()
    if not cleaned_text:
        return False
    return cleaned_text == cleaned_text[::-1]
    
def create_report(title, scores):
    """Takes a report title and a list of scores. Use calculate_average() and find_max_and_min() internally.
    returns a formated string report (NOT a print-a return)."""
    if not scores:
        return "No scores available."
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)
    report = f"Report: {title}\n"
    report += f"Average: {average:.2f}\n"
    report += f"Max: {max_value}\n"
    report += f"Min: {min_value}\n"
    return report
    
# === Test Section ===

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    honors = []
    
    print(f"Average: {calculate_average(test_scores):.2f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))
    print(create_report("Honors Scores", honors))

    # === Edge Case Tests ===
    print("\n--- Empty list ---")
    print(f"calculate_average([]): {calculate_average([])}  (expected 0)")
    print(f"find_max_and_min([]): {find_max_and_min([])}  (expected (0, 0))")

    print("\n--- count_occurrences with repeats ---")
    print(f"Count of 3 in [3, 1, 3, 2, 3]: {count_occurrences([3, 1, 3, 2, 3], 3)}  (expected 3)")
    print(f"Count of 'a' in ['a', 'b', 'a']: {count_occurrences(['a', 'b', 'a'], 'a')}  (expected 2)")
    print(f"Count of 9 in [1, 2, 3]: {count_occurrences([1, 2, 3], 9)}  (expected 0)")

    print("\n--- is_palindrome edge cases ---")
    print(f"'race car': {is_palindrome('race car')}  (expected True)")
    print(f"'A man a plan a canal Panama': {is_palindrome('A man a plan a canal Panama')}  (expected True)")
    print(f"'a': {is_palindrome('a')}  (expected True)")
    print(f"'RaceCar': {is_palindrome('RaceCar')}  (expected True)")
    print(f"'Hello': {is_palindrome('Hello')}  (expected False)")
    
    
