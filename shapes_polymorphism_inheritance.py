import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area (self):
        pass
    def __str__(self):
        return self.__class__.__name__

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi*self.radius**2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length=length
    def calculate_area(self):
        return self.length*self.width
    
shapes = [Circle(5), Rectangle(4, 5)]
for shape in shapes:
    print(f"The area of {shape} is: {shape.calculate_area():.2f}")
    