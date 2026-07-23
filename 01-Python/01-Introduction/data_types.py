'''
Data types in Python
In Python, data types are used to define the type of data that a variable can hold.Variables can store data of different types, and different types can do different things.
Data types in Python can be categorized into several classes, including:
1. Numeric types: int, float, complex
2. Sequence types: list, tuple, range
3. Text type: str
4. Set types: set, frozenset
5. Mapping type: dict
6.Boolean type: bool
7. Binary types: bytes, bytearray, memoryview
8. None type: NoneType

'''

#Numeric types:
#1. int: Integer type, used to represent whole numbers.
x = 5
print(x)  # Output: 5
print(type(x))  # Output: <class 'int'>

#2. float: Floating-point type, used to represent decimal numbers.
y = 3.14
print(y)  # Output: 3.14
print(type(y))  # Output: <class 'float'>

#3. complex: Complex number type, used to represent numbers with a real and imaginary part.
z = 2 + 3j  
print(z)  # Output: (2+3j)
print(type(z))  # Output: <class 'complex'>

#Sequence types:
#1. list: List type, used to represent an ordered collection of items.
my_list = [1, 2, 3]
print(my_list)  # Output: [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>

#2. tuple: Tuple type, used to represent an ordered collection of items that cannot be changed (immutable).
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
print(type(my_tuple))  # Output: <class 'tuple'>

#3. range: Range type, used to represent a sequence of numbers.
my_range = range(5)
print(my_range)  # Output: range(0, 5)
print(type(my_range))  # Output: <class 'range'>

#Text type:
#1. str: String type, used to represent text.
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!
print(type(my_string))  # Output: <class 'str'>

#set types:
#1. set: Set type, used to represent an unordered collection of unique items.
my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>

#2. frozenset: Frozenset type, used to represent an unordered collection of unique items that cannot be changed (immutable).
my_frozenset = frozenset([1, 2, 3])
print(my_frozenset)  # Output: frozenset({1, 2, 3})
print(type(my_frozenset))  # Output: <class 'frozenset'>

#Mapping type:
#1. dict: Dictionary type, used to represent a collection of key-value pairs.
my_dict = {"name": "John", "age": 30}
print(my_dict)  # Output: {'name': 'John', 'age': 30}
print(type(my_dict))  # Output: <class 'dict'>

#Boolean type:
#1. bool: Boolean type, used to represent True or False values.
my_bool = True
print(my_bool)  # Output: True
print(type(my_bool))  # Output: <class 'bool'>

#Binary types:
#1. bytes: Bytes type, used to represent a sequence of bytes.
my_bytes = b"Hello, World!"
print(my_bytes)  # Output: b'Hello, World!'
print(type(my_bytes))  # Output: <class 'bytes'>

#2. bytearray: Bytearray type, used to represent a mutable sequence of bytes.
my_bytearray = bytearray(b"Hello, World!")
print(my_bytearray)  # Output: bytearray(b'Hello, World!')
print(type(my_bytearray))  # Output: <class 'bytearray'>

#3. memoryview: Memoryview type, used to represent a view of a memory buffer.
my_memoryview = memoryview(b"Hello, World!")
print(my_memoryview) # Output: <memory at 0x7f8c8c8c8c8c>
print(type(my_memoryview))  # Output: <class 'memoryview'>

#None type:
#1. NoneType: None type, used to represent the absence of a value or a null value.
my_none = None
print(my_none)  # Output: None
print(type(my_none))  # Output: <class 'NoneType'>