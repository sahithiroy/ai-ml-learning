'''
Type Casting in Python
Type casting is the process of converting a value from one data type to another.
Python provides several built-in functions for type casting:
1. int(): Converts a value to an integer.
2. float(): Converts a value to a floating-point number.
3. str(): Converts a value to a string.
4. bool(): Converts a value to a boolean.
'''

# Converting to integer
x = float("3.14")
y = int(x)
print(y)  # Output: 3
print(type(y))  # Output: <class 'int'>

# Converting to float
x = int("5")
y = float(x)
print(y)  # Output: 5.0
print(type(y))  # Output: <class 'float'>

# Converting to string
x = 10
y = str(x)
print(y)  # Output: "10"
print(type(y))  # Output: <class 'str'>

# Converting to boolean
x = 0
y = bool(x)
print(y)  # Output: False
print(type(y))  # Output: <class 'bool'>