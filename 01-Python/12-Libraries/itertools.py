"""Examples for the itertools module.

The itertools module helps work with iterators and combinations.
"""

from itertools import count, cycle, islice

for i in count(1, 2):
    print(i)  # Output: 1, 3, 5, ...
    if i >= 5:
        break

print(list(islice(cycle([1, 2]), 5)))  # Output: [1, 2, 1, 2, 1]
