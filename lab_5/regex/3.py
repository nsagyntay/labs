'''Write a Python program to find sequences 
of lowercase letters joined with a underscore.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def find_low_underscore(s):
    res = r"[a-z]+(?:_[a-z]+)*"
    return re.findall(res, s)

print(find_low_underscore(text))
