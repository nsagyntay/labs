#Write a Python program to subtract
#  five days from current date
from datetime import datetime, timedelta

cd = datetime.now()
five_days = cd - timedelta(days=5)

print("Current date:", cd.strftime("%Y-%m-%d"))
print("Five days from current date:", five_days.strftime("%Y-%m-%d"))
