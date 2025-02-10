#Implement a generator that returns 
# all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n: "))
for num in countdown(n):
    print(num, end=" ")
