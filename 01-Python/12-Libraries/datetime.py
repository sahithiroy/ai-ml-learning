"""Examples for the datetime module.

The datetime module helps work with dates and times.
"""

from datetime import datetime, timedelta

now = datetime.now()
print(now)                       # Output: current date and time
print(now.year)                 # Output: current year
print(now + timedelta(days=5))  # Output: date 5 days from now
