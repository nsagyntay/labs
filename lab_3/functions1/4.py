'''You are given list of numbers separated by spaces.
 Write a function filter_prime which will take list
of numbers as an agrument and returns only 
prime numbers from the list.'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes
numbers = list(map(int, input("Введите числа через пробел: ").split()))
print("prime numbers:", filter_prime(numbers))
