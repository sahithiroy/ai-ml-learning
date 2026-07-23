'''
Recursion:
A function calling itself to solve smaller parts of a problem.

Real-world use:
We use recursion for problems that can be broken into smaller similar problems.
Example: calculating factorial or traversing folders.

Code:
'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Output: 120
print(factorial(5))
