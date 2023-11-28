#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Print the value of the number
print(f"{number}", end=" ")
# Check whether the number is positive, zero, or negative
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
