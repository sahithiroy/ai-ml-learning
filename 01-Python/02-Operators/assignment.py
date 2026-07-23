'''
Assignment Operators in Python
Assignment operators are used to assign values to variables. Python supports the following assignment operators:

1. **Simple Assignment (=)**: Assigns the value of the right operand to the left operand.
2. **Addition Assignment (+=)**: Adds the right operand to the left operand and assigns the result to the left operand.
3. **Subtraction Assignment (-=)**: Subtracts the right operand from the left operand and assigns the result to the left operand.
4. **Multiplication Assignment (*=)**: Multiplies the left operand by the right operand and assigns the result to the left operand.
5. **Division Assignment (/=)**: Divides the left operand by the right operand and assigns the result to the left operand.
6. **Floor Division Assignment (//=)**: Performs floor division on the left operand by the right operand and assigns the result to the left operand.
7. **Modulus Assignment (%=)**: Computes the modulus of the left operand by the right operand and assigns the result to the left operand.
8. **Exponentiation Assignment (**=)**: Raises the left operand to the power of the right operand and assigns the result to the left operand.
9. **Bitwise AND Assignment (&=)**: Performs a bitwise AND operation on the left operand by the right operand and assigns the result to the left operand.
10. **Bitwise OR Assignment (|=)**: Performs a bitwise OR operation on the left operand by the right operand and assigns the result to the left operand.
11. **Bitwise XOR Assignment (^=)**: Performs a bitwise XOR operation on the left operand by the right operand and assigns the result to the left operand.
12. **Bitwise Right Shift Assignment (>>=)**: Performs a bitwise right shift operation on the left operand by the right operand and assigns the result to the left operand.
13. **Bitwise Left Shift Assignment (<<=)**: Performs a bitwise left shift operation on the left operand by the right operand and assigns the result to the left operand.
14. **Walrus Operator (:=)**: Assigns a value to a variable as part of an expression. This operator is available in Python 3.8 and later versions.
'''
# Simple Assignment
a = 10
print("Simple Assignment:", a)  # Output: 10

# Addition Assignment
a += 5
print("Addition Assignment:", a)  # Output: 15

# Subtraction Assignment
a -= 5
print("Subtraction Assignment:", a)  # Output: 10

# Multiplication Assignment
a *= 5
print("Multiplication Assignment:", a)  # Output: 50

# Division Assignment
a /= 5
print("Division Assignment:", a)  # Output: 10.0

# Floor Division Assignment
a //= 3
print("Floor Division Assignment:", a)  # Output: 3.0

# Modulus Assignment
a %= 3
print("Modulus Assignment:", a)  # Output: 0.0

# Exponentiation Assignment
a **= 2
print("Exponentiation Assignment:", a)  # Output: 0.0

# Bitwise AND Assignment
a = 5  # Binary: 0101
a &= 3  # Binary: 0011
print("Bitwise AND Assignment:", a)  # Output: 1 (Binary: 0001)

# Bitwise OR Assignment
a |= 2  # Binary: 0010
print("Bitwise OR Assignment:", a)  # Output: 3 (Binary: 0011)

# Bitwise XOR Assignment
a ^= 1  # Binary: 0001
print("Bitwise XOR Assignment:", a)  # Output: 2 (Binary: 0010)

# Bitwise Right Shift Assignment
a >>= 1  # Binary: 0010
print("Bitwise Right Shift Assignment:", a)  # Output: 1 (Binary: 0001)

# Bitwise Left Shift Assignment
a <<= 1  # Binary: 0001
print("Bitwise Left Shift Assignment:", a)  # Output: 2 (Binary: 0010)

# Walrus Operator
# The walrus operator allows you to assign a value to a variable as part of an expression
name = "Alice"
if (n := len(name)) > 5:
    print(f"The name is too long ({n} characters).")
#output: The name is too long (5 characters).