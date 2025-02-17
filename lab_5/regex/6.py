'''Write a Python program to replace all occurrences of
 space, comma, or dot with a colon.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def replace_space_comma_dot(s):
    res = r"[ ,.]"
    return re.sub(res, ":", s)

print(replace_space_comma_dot(text))