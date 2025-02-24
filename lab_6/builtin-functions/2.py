#Write a Python program with builtin
#  function that accepts a string and
#  calculate the number of upper case
#  letters and lower case letters
def count_case():
    s = input("string:")
    upp = 0
    low = 0
    for c in s:
        if c.isupper():
            upp += 1
        elif c.islower():
            low += 1
    print(f"Uppercase:{upp},Lowercase:{low}")
count_case()