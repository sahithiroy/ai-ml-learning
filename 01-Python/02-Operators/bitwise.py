'''
Bitwise Operators in Python
Bitwise operators are used to perform bit-level operations on integers. Python supports the following bitwise operators:
1. **Bitwise AND (&)**: Performs a bitwise AND operation between two integers.
2. **Bitwise OR (|)**: Performs a bitwise OR operation between two integers
3. **Bitwise XOR (^)**: Performs a bitwise XOR operation between two integers.
4. **Bitwise NOT (~)**: Performs a bitwise NOT operation on an integer,
5. **Bitwise Right Shift (>>)**: Shifts the bits of an integer to the right by a specified number of positions.
6. **Bitwise Left Shift (<<)**: Shifts the bits of an integer to the left by a specified number of positions.
'''

# Bitwise AND
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Binary: 0001
print("Bitwise AND:", result)  # Output: 1

# Bitwise OR
result = a | b  # Binary: 0111
print("Bitwise OR:", result)  # Output: 7

# Bitwise XOR
result = a ^ b  # Binary: 0110  
print("Bitwise XOR:", result)  # Output: 6

# Bitwise NOT
result = ~a  # Binary: 1010 (two's complement)
print("Bitwise NOT:", result)  # Output: -6

# Bitwise Right Shift
result = a >> 1  # Binary: 0010
print("Bitwise Right Shift:", result)  # Output: 2

# Bitwise Left Shift
result = a << 1  # Binary: 1010
print("Bitwise Left Shift:", result)  # Output: 10