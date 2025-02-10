#Write a Python program to calculate
# the area of a trapezoid.

#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print("Expected Output:", area)
