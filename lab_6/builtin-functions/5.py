#Write a Python program with builtin 
# function that returns True if all 
# elements of the tuple are true.
def all_true():
    t = tuple(map(int, input("tuple:").split()))
    print("All elements are True:", all(t))

all_true()