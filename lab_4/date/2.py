#Write a Python program to print 
# yesterday, today, tomorrow
from datetime import datetime, timedelta

ty = datetime.now()
y = ty - timedelta(days=1)
tw = ty + timedelta(days=1)

print("Yesterday:", y.strftime("%Y-%m-%d"))
print("Today:", ty.strftime("%Y-%m-%d"))
print("Tomorrow:", tw.strftime("%Y-%m-%d"))
