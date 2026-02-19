# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    aString = ""
    # mengyhapus white space dan punctuation
    for i in s:
        if i not in " ,.":
            aString += i

    cleanString = aString.lower()
    
    # char = len(cleanString)
    # slicing, rumus slicing di python data[start:end:step]
    reverseWords = cleanString[::-1]

    return cleanString == reverseWords

# You can test your function with print statements below
# Example:
# print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))  # Expected output: False
