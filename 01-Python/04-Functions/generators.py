'''
Generators:
Generators create values one at a time and save memory.

Real-world use:
We use generators for large data sequences where we do not need everything at once.
Example: reading large files or generating numbers lazily.

Code:
'''

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for value in count_up_to(3):
    print(value)

# Output:
# 1
# 2
# 3
