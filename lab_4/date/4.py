#Write a Python program to calculate
#  two date difference in seconds.
from datetime import datetime

d1 = datetime.fromisoformat(input("Enter second date (YYYY-MM-DD HH:MM:SS): "))
d2 = datetime.fromisoformat(input("Enter second date (YYYY-MM-DD HH:MM:SS): "))

m = abs((d2 - d1).total_seconds())

print("Difference in seconds:", m)
