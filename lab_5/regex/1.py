'''Write a Python program that matches a string
 that has an 'a' followed by zero or more 'b''s.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def match_a_by_b(s):
    res = r"ab*"
    return re.fullmatch(res, s)

print(match_a_by_b("abbb"))
