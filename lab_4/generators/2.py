#Write a program using generator to 
# print the even numbers between 0 
# and n in comma separated form where
#  n is input from console.
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("n: "))
print(",".join(even_generator(n)))
