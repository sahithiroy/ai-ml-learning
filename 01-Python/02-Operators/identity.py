'''
Identity operators in Python are used to compare the memory identity of two objects.

Operators:
- is      : returns True if both variables point to the same object
- is not  : returns True if both variables do not point to the same object

Examples:
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True
print(a is c)        # False
print(a is not c)    # True

x = 10
y = 10
print(x is y)        # True

name1 = "Alice"
name2 = "Alice"
print(name1 is name2)  # True
