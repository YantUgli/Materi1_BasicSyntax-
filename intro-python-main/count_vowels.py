# count_vowels.py

def count_vowels(s: str) -> int:
    """
    This function counts the number of vowels (a, e, i, o, u) in a given string `s`.

    Args:
    - s (str): The input string.

    Returns:
    - int: The number of vowels in the string.

    Examples:
    - count_vowels("hello world") should return 3
    - count_vowels("python") should return 1
    """
    # Implement your solution here
    total = 0

    # cara 1
    # for x in s:
    #     if x == "e" or x == "a" or x == "i" or x == "o" or x == "u":
    #         total += 1

    # better untuk cleaning vocals dan bahkan bisa juga punctuation
    for x in s:
        if x in "aiueo":
            total += 1
    
    
    return total
# You can test your function with print statements below
# Example:
# print(count_vowels("hello world"))  # Expected output: 3
# print(count_vowels("python"))  # Expected output: 1
