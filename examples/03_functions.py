# Example 03 – Functions
# Functions let you reuse blocks of code.

def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0


# Call the functions
print(greet("Bob"))
print("3 + 4 =", add(3, 4))
print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))
