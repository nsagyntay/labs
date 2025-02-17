'''Write a Python program to convert a given camel 
case string to snake case.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def camel_to_snake(s):
    res = r"([a-z])([A-Z])"
    return re.sub(res, r"\1_\2", s).lower()

print(camel_to_snake("camelCaseString"))
