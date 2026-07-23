"""List comprehension in Python

List comprehension is a short way to create lists.
It is used to make code shorter and easier to read.

Syntax:
[value for item in iterable]
"""

# Example 1: Create a list of squares
squares = [x * x for x in range(1, 6)]
print(squares)

# Example 2: Create a list with a condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# Example 3: Create a list from a string
chars = [ch for ch in "python"]
print(chars)
