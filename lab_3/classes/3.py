#Define a class named Rectangle which 
# inherits from Shape class from task 2. 
# Class instance can be constructed by a
#length and width. The Rectangle class
#has a method which can compute the area.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

length = int(input("Enter the length of the square: "))
square = Square(length)
print("Area of the square:", square.area())

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("Area of the rectangle:", rectangle.area())

shape = Shape()
print("Area of the shape:", shape.area())
