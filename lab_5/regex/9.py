'''Write a Python program to insert spaces between words 
starting with capital letters.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def spaces_capitals(s):
    res = r"([a-z])([A-Z])"
    return re.sub(res, r"\1 \2", s)

print(spaces_capitals("HelloWorldHowAreYou"))
