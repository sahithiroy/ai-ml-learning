"""Dictionary comprehension in Python

Dictionary comprehension is a short way to create dictionaries.
It is similar to list comprehension, but it creates key-value pairs.

Syntax:
{key: value for item in iterable}
"""

# Example 1: Create a dictionary of squares
squares = {x: x * x for x in range(1, 6)}
print(squares)

# Example 2: Create a dictionary with a condition
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# Example 3: Create a dictionary from a list of tuples
items = [("apple", 3), ("banana", 5), ("orange", 2)]
fruit_count = {fruit: count for fruit, count in items}
print(fruit_count)
