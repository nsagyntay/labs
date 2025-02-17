'''Write a Python program that matches a string that
 has an 'a' followed by anything, ending in 'b'.'''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def match_a_any_b(s):
    res = r"a.*b$"
    return re.fullmatch(res, s)

print(match_a_any_b("axb"))