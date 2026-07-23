"""Example of logging exceptions."""

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Division by zero error: %s", e)
    print("Error logged.")
