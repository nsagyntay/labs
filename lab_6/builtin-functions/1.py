#Write a Python program with builtin 
#function to multiply all the numbers
#in a list

def multiply_list():
    n= list(map(int, input("n: ").split()))
    result = 1
    for num in n:
        res *= num
    print("Product:", res)
    multiply_list()