'''Write a python program to convert snake case string
 to camel case string.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def snake_to_camel(s):
    p = s.split("_")
    return p[0] + "".join(word.capitalize() for word in p[1:])

print(snake_to_camel("snake_case_string"))
