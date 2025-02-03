#Write a program which can filter
#  prime numbers in a list by using 
# filter function. Note: Use lambda 
# to define anonymous functions.
def filter_prime_numbers(n):
    return list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), n))
num = input("Enter numbers")
n = list(map(int, num.split()))
prime_numbers = filter_prime_numbers(n)
print("prime numbers:", prime_numbers)
