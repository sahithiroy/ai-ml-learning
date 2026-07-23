"""Day 9: Generators

Topics:
- yield: pauses a function and returns one value at a time
- generator expressions: concise syntax for creating generators
- lazy evaluation: values are produced only when needed
- generator pipeline: several generators work together to process data step by step

Generators are useful when working with large data because they do not store
all values in memory at once.
"""

from itertools import islice


def count_up_to(n):
    """Yield numbers from 0 up to n - 1."""
    i = 0
    while i < n:
        yield i
        i += 1


# 1. yield
# A generator function uses yield instead of return to produce a sequence.
print("Example 1: yield")
for value in count_up_to(5):
    print(value)
print()


# 2. Generator expressions
# A generator expression is a compact way to create a generator.
print("Example 2: generator expression")
squares = (x * x for x in range(1, 6))
print(list(squares))
print()


# 3. Lazy evaluation
# Values are generated only when the next item is requested.
print("Example 3: lazy evaluation")
lazy_numbers = count_up_to(10)
print(next(lazy_numbers))
print(next(lazy_numbers))
print(next(lazy_numbers))
print()


# 4. Generator pipeline
# We can pass output of one generator into another generator.
print("Example 4: generator pipeline")

def even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


def square_numbers(numbers):
    for n in numbers:
        yield n * n

values = [1, 2, 3, 4, 5, 6, 7, 8]
pipeline = square_numbers(even_numbers(values))
print(list(pipeline))
print()


# 5. Infinite Fibonacci generator
# This generator never ends, so we use islice to take a few values.
print("Example 5: infinite Fibonacci")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(islice(fibonacci(), 10)))
print()


# 6. Infinite prime generator
print("Example 6: infinite prime numbers")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print(list(islice(primes(), 10)))
print()


# 7. Read a huge file line by line
# This is memory-friendly because one line is read at a time.
print("Example 7: read huge file line by line")

def read_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")

# Uncomment the next two lines if you want to test it on a real file.
# for line in read_lines("sample.txt"):
#     print(line)
print()


# Practice problems
# 1. Infinite Fibonacci -> implemented above
# 2. Infinite prime numbers -> implemented above
# 3. Read huge file line by line -> implemented above
# 4. Generator pipeline -> implemented above
# 5. Number stream generator -> create numbers like 1, 2, 3, 4, ...

print("Practice: number stream generator")

def number_stream(start=1):
    current = start
    while True:
        yield current
        current += 1

print(list(islice(number_stream(), 8)))
