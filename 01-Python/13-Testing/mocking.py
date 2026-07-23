"""Example of mocking.

Mocking is used to replace parts of your code during testing.
"""

from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()
mock_obj.method.return_value = 42

print(mock_obj.method())  # Output: 42
