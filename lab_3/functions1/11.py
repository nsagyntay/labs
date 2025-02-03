#Write a Python function that 
#checks whether a word or phrase
#is palindrome or not. Note: A 
#palindrome is word, phrase, or 
#sequence that reads the same
#backward as forward, e.g., madam
def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
ch = input("Enter a word or phrase: ")
if is_palindrome(ch):
    print("palindrome")
else:
    print("not palindrome")