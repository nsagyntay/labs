'''Write a Python program to split a 
string at uppercase letters.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()  

def split_at_uppercase(s):
    res = r"[A-Z][a-z]*"
    return re.findall(res, s)

print(split_at_uppercase("HelloWorld"))
