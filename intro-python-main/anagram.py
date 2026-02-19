# anagram.py

def is_anagram(s1: str, s2: str) -> bool:
    """
    This function checks if the two given strings `s1` and `s2` are anagrams.
    
    Two strings are anagrams if they contain the same characters with the same frequencies,
    ignoring spaces and capitalization.
    
    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.
    
    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    
    Examples:
    - is_anagram("Listen", "Silent") should return True
    - is_anagram("hello", "billion") should return False
    """
    # Step 1: Clean the strings by removing non-alphanumeric characters and converting to lowercase
    # Step 2: Compare the character counts of both cleaned strings
    
    # Implement your solution here

    # menghapus white space dan tanda baca seperti !
    lower1 = s1.lower().replace(" ", "").replace("!", "")
    lower2 = s2.lower().replace(" ", "").replace("!", "")

    clean1 = ""
    clean2 = ""

    # menghapus tanda baca(sepertinya penting ga penting sih)
    for x in lower1:
        if x not in 'aeiou':
            clean1 += x

    for x in lower2:
        if x not in 'aeiou':
            clean2 += x
    
    # masukan frekuensi muncul setiap character ke dalam dictionary/json
    frekuensi1 = {}
    frekuensi2 = {}
    if len(clean1) == len(clean2):
        for x in clean1:
            # .get yang ada di sini, x sebagai nilai juga sudah ada, dan 0 sebagai nilai default
            frekuensi1[x] = frekuensi1.get(x, 0) + 1

        for x in clean2:
            frekuensi2[x] = frekuensi2.get(x, 0) + 1
    else :
        return False
    
    # bandingkan hasil dict1 dan dict2
    return frekuensi1 == frekuensi2


# You can test your function with print statements below
# Example:
# print(is_anagram("Listen", "Silent"))  # Expected output: True
# print(is_anagram("hello", "billion"))  # Expected output: False
