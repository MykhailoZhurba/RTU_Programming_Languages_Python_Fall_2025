"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    char_count = len(text)

    # 2. word count
    words = text.split()
    word_count = len(words)

    # 3. whether it contains the word "Python" (case-insensitive)
    # We convert the whole text to lowercase to make the search case-insensitive
    has_python = "python" in text.lower()

    # Return results as a tuple
    return (char_count, word_count, has_python)

if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    sentence = input("Enter a sentence to analyze: ")

    if not sentence.strip():
        print("You did not enter anything.")
    else:
        # call function and unpack the tuple
        char_count, word_count, has_python = analyze_sentence(sentence)

        # print results
        print("\n--- Analysis Results ---")
        print(f"Total Characters: {char_count}")
        print(f"Total Words: {word_count}")
        print(f"Contains 'Python': {has_python}")
