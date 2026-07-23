"""Example of iterators in Python.

An iterator is an object that allows you to traverse through a collection one item at a time.
An iterator in Python is an object used to traverse through all the elements of a collection (like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, which involves two key methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends.

Iterator vs Iterable
Although the terms iterator and iterable sound similar, they are not the same.
An iterable is any object that can return an iterator, while an iterator is the actual object that performs iteration one element at a time.

Benefits:
Lazy Evaluation: Elements are produced on demand rather than stored entirely in system RAM. This allows you to safely parse multi-gigabyte server logs or manage infinite data streams without crashing your machine.
Stateful Traversal: They natively remember where they left off in a stream of information.
"""

numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3



# Problem 1: Countdown iterator
class CountDown:
    def __init__(self, limit):
        self.current = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


print("Countdown:")
for num in CountDown(5):
    print(num)  # Output: 5, 4, 3, 2, 1


# Problem 2: Even number iterator
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.n = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.limit:
            raise StopIteration
        x = self.n
        self.n += 2
        return x


print("Even numbers:")
even = EvenNumbers(10)
for num in even:
    print(num)  # Output: 2, 4, 6, 8, 10


# Problem 3: Fibonacci iterator
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value


print("Fibonacci:")
for num in FibonacciIterator(7):
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8


# Problem 4: Prime iterator
class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.limit:
            if self._is_prime(self.current):
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration

    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


print("Prime numbers:")
for num in PrimeIterator(20):
    print(num)  # Output: 2, 3, 5, 7, 11, 13, 17, 19


# Problem 5: Alphabet iterator
class AlphabetIterator:
    def __init__(self, start='A', end='E'):
        self.current = ord(start)
        self.end = ord(end)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = chr(self.current)
        self.current += 1
        return value


print("Alphabet:")
for ch in AlphabetIterator():
    print(ch)  # Output: A, B, C, D, E
