#Write a Python program with builtin 
# function that checks whether a passed
#  string is palindrome or not.
def is_palindrome():
    s = input("string:")
    print("Palindrome:", s == s[::-1])

is_palindrome()