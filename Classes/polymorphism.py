# Polymorphism - many forms

# Method/function/operators have same name that can be executed in different forms

# Example - len() function

import math

class Polygon:
    def __init__(self):
        print("Calculate the area of the polygon")

    def area(self):
        print("Please subclass method")

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Square(Polygon):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2

    
shapes = [Rectangle(10, 5), Square(10), Circle(7)]

for shape in shapes:
    print(shape.area())


    



    
