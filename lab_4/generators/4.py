#Implement a generator called squares
#  to yield the square of all numbers
#  from (a) to (b). Test it with a 
# "for" loop and print each of the
#  yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a, b = map(int, input("a , b: ").split())
for sq in squares(a, b):
    print(sq, end=" ")
