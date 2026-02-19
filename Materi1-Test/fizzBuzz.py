# fizzbuzz.py

def fizzbuzz(n: int) -> list:
    """
    This function returns a list of strings with the numbers from 1 to `n`.
    But for multiples of three, return "Fizz" instead of the number and for the multiples of five, return "Buzz".
    For numbers which are multiples of both three and five, return "FizzBuzz".

    Args:
    - n (int): The upper limit of the range (inclusive).

    Returns:
    - list: A list of strings representing the FizzBuzz sequence.
    
    Examples:
    - fizzbuzz(15) should return ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    """
    # Implement your solution here
    hasil = []
    # kenapa n+1 ? karena biar hasil akhirnya ga kurang, karena index mulai dari 0, jadi dari 1 - angka yang diperlukan
    for i in range(1, n+1):

        # jika habis dibagi 5 dan 3 secara bersamaan
        if i % 5 == 0 and i % 3 ==  0:
            hasil.append("FizzBuzz")

        # jika habis dibagi 5
        elif i % 5 == 0:
            hasil.append("Buzz")
            
        # jika habis dibagi 3
        elif i % 3 == 0:
            hasil.append("Fizz")
        else:
            hasil.append(str(i))
        

    return hasil

# You can test your function with print statements below
# Example:
# print(fizzbuzz(15))  # Expected output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
