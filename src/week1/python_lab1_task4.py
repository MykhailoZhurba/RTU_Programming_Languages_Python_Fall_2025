"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    # TODO: implement
    count = 0
    for char in text:
        if not char.isspace():
            count += 1
    return count


def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    words = text.split()
    return len(words)

def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    found_numbers = re.findall(r'\d+', text)
    # Convert the found strings to integers
    return [int(num) for num in found_numbers]

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    char_count = count_characters(text)

    word_count = count_words(text)

    numbers = extract_numbers(text)
    total_sum = sum(numbers)
    num_count = len(numbers)

    if num_count > 0:
        average = total_sum / num_count
    else:
        average = 0.0

    return {
        "char_count": char_count,
        "word_count": word_count,
        "numbers_found": numbers,
        "sum_of_numbers": total_sum,
        "average_of_numbers": average
    }


if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    user_text = input("Enter some text with numbers (e.g., 'I have 10 apples and 5 oranges'): ")

    if not user_text.strip():
        print("You did not enter anything.")
    else:
        # call analyze_text()
        analysis = analyze_text(user_text)

        # print results
        print("\n--- Analysis Results ---")
        print(f"Non-Space Characters: {analysis['char_count']}")
        print(f"Total Words: {analysis['word_count']}")
        print(f"Numbers Found: {analysis['numbers_found']}")
        print(f"Sum of Numbers: {analysis['sum_of_numbers']}")
        print(f"Average of Numbers: {analysis['average_of_numbers']:.2f}")

