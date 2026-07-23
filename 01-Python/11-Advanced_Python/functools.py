"""Example of functools in Python.

functools provides helpers for higher-order functions.
"""

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 10
