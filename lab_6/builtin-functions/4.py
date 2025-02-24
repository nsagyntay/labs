#Write a Python program that invoke
#square root function after specific 
#milliseconds.

# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 
# miliseconds is 158.42979517754858
import time
import math
def delayed_sqrt():
    n = int(input("n:"))
    delay_ms = int(input("delay in ms:"))
    time.sleep(delay_ms / 1000)
    print(f"Square root of {n} after {delay_ms} ms is {math.sqrt(n)}")
delayed_sqrt()