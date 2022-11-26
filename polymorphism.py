class Shape:

    def get_area(self):
        return "No Implementation"


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

shape = Shape()
print(shape.get_area())
triangle = Triangle(10,5)
rectangle = Rectangle(10,4)
#
for i in [triangle,rectangle]:
    if isinstance(i,Triangle):
        print("Triangle Area =",i.get_area())
    elif isinstance(i,Rectangle):
        print("Rectangle Area =", i.get_area())

def add(x, y, z=0):
    return x + y + z


print(add(10, 20))
print(add(10, 20, 30))
