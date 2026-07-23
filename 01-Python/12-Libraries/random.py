"""Examples for the random module.

The random module is used to generate random values.
"""

import random

print(random.random())          # Output: a random float between 0 and 1
print(random.randint(1, 10))    # Output: a random integer between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Output: one random item
