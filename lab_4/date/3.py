#Write a Python program to drop
#  microseconds from datetime.
from datetime import datetime

cd = datetime.now().replace(microsecond=0)
print("Datetime without microseconds:", cd)
