#Write the definition of a Point class.
#  Objects from this class should have a
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points
import math
class Point:
    def __init__(a, x, y):
        a.x = x
        a.y = y
    def show(a):
        print(f"Point({a.x}, {a.y})")
    def move(a, new_x, new_y):
        a.x = new_x
        a.y = new_y
    def dist(a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
x1, y1 = map(int, input("Enter coordinates for first point (x y): ").split())
x2, y2 = map(int, input("Enter coordinates for second point (x y): ").split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p1.show()
p2.show()
print("Distance:", p1.dist(p2))