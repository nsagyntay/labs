#Create a generator that generates
#  the squares of numbers up to 
# some number N.
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input("N: "))
for square in square_generator(N):
    print(square, end=" ")
