'''
Decorators:
Decorators add extra behavior to a function without changing its code.

Real-world use:
We use decorators for logging, authentication, or timing functions.
Example: adding a message before running a function.

Code:
'''

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

# Output:
# Before function
# Hello
# After function
say_hello()
