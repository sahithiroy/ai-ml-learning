"""Day 12: Typing

Topics:
- typing
- Optional
- Union
- List
- Dict
- Tuple
- Callable
- TypeAlias

Type hints make code easier to read, understand, and maintain.
"""

# 1. Basic type hints
print("Example 1: basic type hints")

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # Output: 5
print()


# 2. Optional
print("Example 2: Optional")

def greet(name=None) -> str:
    if name is None:
        return "Hello!"
    return f"Hello, {name}!"

print(greet())       # Output: Hello!
print(greet("Alice"))  # Output: Hello, Alice!
print()


# 3. Union
print("Example 3: Union")

def format_value(value) -> str:
    return str(value)

print(format_value(10))     # Output: 10
print(format_value("ten"))  # Output: ten
print()


# 4. List
print("Example 4: List")

def total(numbers) -> int:
    return sum(numbers)

print(total([1, 2, 3, 4]))  # Output: 10
print()


# 5. Dict
print("Example 5: Dict")

def user_info(user) -> str:
    return f"Name: {user['name']}, Age: {user['age']}"

print(user_info({"name": "Bob", "age": "25"}))  # Output: Name: Bob, Age: 25
print()


# 6. Tuple
print("Example 6: Tuple")

def point() -> tuple:
    return (10, 20)

print(point())  # Output: (10, 20)
print()


# 7. Callable
print("Example 7: Callable")

def apply_function(func, value: int) -> int:
    return func(value)

print(apply_function(lambda x: x * 2, 5))  # Output: 10
print()


# 8. TypeAlias
print("Example 8: TypeAlias")

UserDict = dict

def describe_user(user: dict) -> str:
    return f"{user['name']} is {user['age']} years old"

print(describe_user({"name": "Ana", "age": 22}))  # Output: Ana is 22 years old
print()


# Practice: Annotate previous projects
print("Practice: annotate a small project example")

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I am {self.name}"


def enroll_students(students) -> list:
    return [student.introduce() for student in students]

students = [Student("Riya", 20), Student("Karan", 22)]
print(enroll_students(students))  # Output: ['Hi, I am Riya', 'Hi, I am Karan']
