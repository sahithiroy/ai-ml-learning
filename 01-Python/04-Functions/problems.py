"""
Solutions to common function practice problems.
Write your own max() function.
Write your own min() function.
Factorial using recursion.
Fibonacci using recursion.
Palindrome checker.
Prime number checker.
Armstrong number.
Perfect number.
GCD and LCM.
Power function without using **.

"""


def my_max(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


def my_min(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")

    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_armstrong(n):
    if n < 0:
        return False

    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


def is_perfect(n):
    if n <= 0:
        return False

    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent cannot be negative")

    result = 1
    for _ in range(exponent):
        result *= base
    return result


if __name__ == "__main__":
    print("max:", my_max([3, 8, 1, 6]))
    print("min:", my_min([3, 8, 1, 6]))
    print("factorial(5):", factorial(5))
    print("fibonacci(7):", fibonacci(7))
    print("palindrome('level'):", is_palindrome("level"))
    print("prime(13):", is_prime(13))
    print("armstrong(153):", is_armstrong(153))
    print("perfect(28):", is_perfect(28))
    print("gcd(24, 36):", gcd(24, 36))
    print("lcm(4, 6):", lcm(4, 6))
    print("power(2, 3):", power(2, 3))

