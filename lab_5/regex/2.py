'''Write a Python program that matches a string 
that has an 'a' followed by two to three 'b' '''

import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

def match_a_2_3_b(s):
    res = r"ab{2,3}"
    return re.fullmatch(res, s)

print(match_a_2_3_b("abb"))


