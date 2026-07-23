"""Day 10: Decorators

Topics:
- Functions as first-class objects
- Nested functions
- Closures
- Function decorators
- Class decorators
- Decorators with arguments
- functools.wraps

A decorator changes the behavior of a function without changing its source code.
"""

import time


def wraps(func):
    """A small version of functools.wraps for this lesson."""
    def decorator(wrapper):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        return wrapper
    return decorator


# 1. Functions as first-class objects
print("Example 1: functions as first-class objects")

def greet(name):
    return f"Hello, {name}!"


def call_function(func, value):
    return func(value)

print(call_function(greet, "Alice"))  # Output: Hello, Alice!
print()


# 2. Nested functions
print("Example 2: nested functions")

def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

my_func = outer_function("Welcome")
my_func()  # Output: Welcome
print()


# 3. Closures
print("Example 3: closures")

def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10
print()


# 4. Function decorators
print("Example 4: function decorators")

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet_message():
    return "hello"

print(greet_message())  # Output: HELLO
print()


# 5. Class decorators
print("Example 5: class decorators")

class Prefixer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return "[INFO] " + self.func(*args, **kwargs)

@Prefixer
def log_message(message):
    return message

print(log_message("saved"))  # Output: [INFO] saved
print()


# 6. Decorators with arguments
print("Example 6: decorators with arguments")

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet_user(name):
    print(f"Hello {name}")

print(greet_user("Bob"))  # Output: Hello Bob
print()


# 7. functools.wraps
print("Example 7: functools.wraps")

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@simple_decorator
def say_hello(name):
    return f"Hello {name}"

print(say_hello.__name__)  # Output: say_hello
print()


# Practice decorators
# 1. Timer
print("Practice 1: timer decorator")

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(0.01)
    return "done"

print(slow_task())  # Output: done
print()


# 2. Logger
print("Practice 2: logger decorator")

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5
print()


# 3. Authentication
print("Practice 3: authentication decorator")

def authenticate(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if required_role == "admin":
                print("Access granted")
            else:
                print("Access denied")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@authenticate("admin")
def secret_action():
    return "secret data"

print(secret_action())  # Output: secret data
print()


# 4. Retry
print("Practice 4: retry decorator")

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"Attempt {attempt + 1} failed: {exc}")
            raise RuntimeError("All attempts failed")
        return wrapper
    return decorator

@retry(3)
def flaky_task():
    raise ValueError("Temporary error")

try:
    flaky_task()
except Exception as exc:
    print(exc)  # Output: All attempts failed
print()


# 5. Cache
print("Practice 5: cache decorator")

def cache(func):
    stored = {}

    @wraps(func)
    def wrapper(*args):
        if args in stored:
            print("Cache hit")
            return stored[args]
        result = func(*args)
        stored[args] = result
        print("Cache miss")
        return result
    return wrapper

@cache
def expensive_square(n):
    return n * n

print(expensive_square(4))  # Output: 16
print(expensive_square(4))  # Output: 16
print()


# 6. Validate input
print("Practice 6: validate input")

def validate_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, int):
                raise TypeError("Only integers are allowed")
        return func(*args, **kwargs)
    return wrapper

@validate_input
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 4))  # Output: 7
print()
