'''
break and continue:
- break stops the loop completely
- continue skips the current iteration

Real-world use:
We use break when we want to stop searching once the result is found.
We use continue when we want to skip an item and continue with the next one.
Example: stop looking for a user when found, or skip invalid data entries.

Example:
'''

for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("---")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
