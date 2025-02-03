'''Write a function that accepts 
string from user and print 
all permutations of that string.'''
def permutations(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[:i] + s[i+1:]
        permutations(left_substr, answer + ch)
s = input("string: ")
permutations(s)



     

        