'''Write a Python program to find the sequences of one
 upper case letter followed by lower case letters.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def upp_followed_low(s):
    res = r"[A-Z][a-z]+"
    return re.findall(res, s)

print(upp_followed_low(text))