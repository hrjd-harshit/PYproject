class Shape:
    def area(self):
        return "this is the area of the shape"

class rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width*self.height

class circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

Rectangle = rectangle(23,55)
print(Rectangle.area())
Circle = circle(23)
print(Circle.area())