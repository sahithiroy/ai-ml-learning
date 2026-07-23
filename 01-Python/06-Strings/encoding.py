"""Example of string encoding and decoding.

Encoding means converting a string into bytes.
Decoding means converting bytes back into a string.
"""

text = "Hello"
encoded = text.encode("utf-8")  # Output: b'Hello'
decoded = encoded.decode("utf-8")  # Output: Hello

print(encoded)
print(decoded)
