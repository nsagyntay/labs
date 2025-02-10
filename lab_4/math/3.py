#Write a Python program to calculate
#  the area of regular polygon.

#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", area)
