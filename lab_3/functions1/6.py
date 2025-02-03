'''Write a function that accepts 
string from user, return a sentence 
with the words reversed.
 We are ready -> ready are We'''
def reverse_word(s):
    words = s.split()
    reverse = ""
    for word in words[::-1]:
        reverse += word + " "
    return reverse.strip()
s = input("string: ")
reverse = reverse_word(s)
print("Reversed string:",reverse)