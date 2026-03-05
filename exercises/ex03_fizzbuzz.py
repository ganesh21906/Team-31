# Exercise 03 – FizzBuzz
#
# Task: Write a function `fizzbuzz(n)` that returns a list of strings
#       for the numbers 1 through n (inclusive) where:
#         - multiples of 3 → "Fizz"
#         - multiples of 5 → "Buzz"
#         - multiples of both 3 and 5 → "FizzBuzz"
#         - everything else → the number as a string
#
# Example: fizzbuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8",
#                           "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        pass  # TODO: append the correct value to result
    return result


# --- Tests (do not modify) ---
if __name__ == "__main__":
    output = fizzbuzz(15)
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]
    assert output == expected, f"Test failed.\nGot:      {output}\nExpected: {expected}"
    print("All tests passed! Great job!")
