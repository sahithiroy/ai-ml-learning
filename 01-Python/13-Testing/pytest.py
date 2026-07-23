"""Example of testing with pytest.

pytest is a popular third-party testing framework.
"""


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
