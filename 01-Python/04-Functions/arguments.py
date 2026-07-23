'''
Function arguments:
Arguments allow us to pass values into functions.

From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the actual value sent to the function when it is called.

Real-world use:
We use arguments when a function needs different input values.
Example: a function that greets a specific person.

Number of Arguments:
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.

Default Parameter Values:
You can give parameters default values so that the function still works if no argument is provided.

Keyword Arguments:
You can send arguments with the key = value syntax.

Mixing Positional and Keyword Arguments:
You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments.

Code:
'''

def greet(name):
    print("Hello", name)

# Output: Hello Alice
greet("Alice")

# Output: Hello Bob
greet("Bob")


def add(a, b):
    return a + b

# Output: 8
print(add(3, 5))


def welcome(name="Guest"):
    print("Welcome", name)

# Output: Welcome Guest
welcome()

# Output: Welcome Sarah
welcome("Sarah")


def describe(person, age):
    print(person, "is", age, "years old")

# Output: Alice is 20 years old
describe("Alice", 20)

# Output: Bob is 25 years old
describe(age=25, person="Bob")

# Output: Charlie is 30 years old
describe("Charlie", age=30)
